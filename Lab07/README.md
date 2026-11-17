# Лабораторна робота №7. Автоматизація мережевих тестів на Python: iperf, subprocess, pytest і paramiko

**Виконав:** Святний Тимофій, група ІО-34

- [`report.pdf`](report.pdf) — звіт (Test Plan TP-IPERF-01, тест-кейси TC-IPERF-01, TC-AUTO-01, TC-AUTO-02, TC-PY-01, TC-PY-02, TC-PY-03, defect reports DEF-ENV-02, DEF-DOC-02, DEF-ENV-03, DEF-TOOL-01)
- [`part1/`](part1/) — частина 1: `iperf_client.py` (запуск клієнта iperf через subprocess), `parser.py` (розбір виводу через `re`)
- [`part2/`](part2/) — частина 2: `conftest.py` (фікстури `server` через paramiko і `client`), `parser.py`, `iperf_test.py` (`class TestSuite`)
- [`screenshots/`](screenshots/) — скриншоти до звіту (термінали PC1 і PC2)
- [`logs/`](logs/) — вивід ручного запуску iperf, скрипта частини 1 і трьох запусків pytest (позитивний, поріг, сервер недоступний)

Запуск частини 2 на PC2: `cd part2 && python3 -m pytest -v iperf_test.py`
(потрібен SSH-доступ до PC1 за ключем `~/.ssh/id_ed25519`).
