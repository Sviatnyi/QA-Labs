"""Фікстури pytest: iperf-сервер на PC1 через SSH (paramiko) і iperf-клієнт на PC2 (subprocess)."""
import os
import re
import subprocess
import time

import paramiko
import pytest

# Дані сервера. Вхід по SSH-ключу, пароль у коді не зберігається.
server_ip = os.environ.get('IPERF_SERVER', '10.0.0.1')
username = os.environ.get('IPERF_USER', 'tymofii')
key_file = os.path.expanduser('~/.ssh/id_ed25519')
# Порт, на якому піднімається сервер (для негативного тесту можна задати інший)
server_port = os.environ.get('IPERF_SERVER_PORT', '5001')
CLIENT_PORT = '5001'
DURATION = int(os.environ.get('IPERF_TIME', '10'))


@pytest.fixture(scope='function')
def server():
    """Підключається до PC1 по SSH, піднімає iperf-сервер, після тесту зупиняє його і закриває SSH."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, key_filename=key_file, timeout=10)
    ssh.exec_command('pkill -x iperf')[1].channel.recv_exit_status()
    _, stdout, _ = ssh.exec_command(
        f'nohup iperf -s -p {server_port} > /tmp/iperf_server.log 2>&1 & echo $!')
    pid = stdout.read().decode().strip()
    time.sleep(1)
    _, stdout, _ = ssh.exec_command(f'kill -0 {pid} && echo running')
    error = '' if 'running' in stdout.read().decode() else 'iperf server did not start'
    yield error
    # teardown – виконується незалежно від результату тесту
    ssh.exec_command(f'kill {pid}')[1].channel.recv_exit_status()
    ssh.close()


@pytest.fixture(scope='function')
def client(server):
    """Запускає iperf-клієнт і повертає (вивід, помилка) для аналізу в тесті."""
    if server:
        return '', server
    proc = subprocess.run(
        ['iperf', '-c', server_ip, '-p', CLIENT_PORT, '-i', '1', '-t', str(DURATION), '-f', 'm'],
        capture_output=True, text=True, timeout=DURATION + 30)
    error = proc.stderr.strip()
    if proc.returncode != 0 and not error:
        error = f'iperf exited with code {proc.returncode}: {proc.stdout.strip()}'
    # iperf 2 додає до помилки мітку часу "on YYYY-MM-DD hh:mm:ss (UTC)" - прибираємо її
    error = re.sub(r'\s+on \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \(\w+\)', '', error)
    return proc.stdout, error
