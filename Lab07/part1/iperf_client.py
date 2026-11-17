"""ЛР №7 (методичка №8, ч. 1): підключення клієнта iperf до сервера через subprocess."""
import re
import subprocess
import sys

import parser

server_ip = '10.0.0.1'      # PC1, сервер піднімається вручну: iperf -s

MIN_TRANSFER = 2            # МБайт
MIN_BITRATE = 20            # Мбіт/с


def client(server_ip, duration=10, interval=1):
    """Запускає iperf-клієнт і повертає (вивід, помилка)."""
    cmd = ['iperf', '-c', server_ip, '-i', str(interval), '-t', str(duration), '-f', 'm']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        out, err = proc.communicate(timeout=duration + 30)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
        err += '\nTimeout: iperf client did not finish'
    # iperf 2 може писати помилку з'єднання у stdout, тому дивимося й на код повернення
    if proc.returncode != 0 and not err:
        err = f'iperf exited with code {proc.returncode}: {out.strip()}'
    # iperf 2 додає до помилки мітку часу "on YYYY-MM-DD hh:mm:ss (UTC)" - прибираємо її
    err = re.sub(r'\s+on \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \(\w+\)', '', err)
    return out, err.strip()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        server_ip = sys.argv[1]
    result, error = client(server_ip)
    if error:
        print('ERROR:', error)
        sys.exit(1)
    result_list = parser.parser(result)
    print(f'Інтервалів: {len(result_list)}; умова: Transfer > {MIN_TRANSFER} MB і Bitrate > {MIN_BITRATE} Mbit/s')
    for value in result_list:
        if value['Transfer'] > MIN_TRANSFER and value['Bitrate'] > MIN_BITRATE:
            print(value)
