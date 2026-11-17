# Тестування та контроль якості вбудованих систем (QA)

**Студент:** Святний Тимофій, група ІО-34

Звіти, скриншоти, конфігурації, захоплення трафіку та код лабораторних робіт з дисципліни.

| № | Тема | Матеріали |
|---|---|---|
| 1 | Ознайомлення з Linux: базові команди терміналу | [Lab01](Lab01/) |
| 2 | Протокол ARP, аналіз трафіку у Wireshark | [Lab02](Lab02/) |
| 3 | Протокол DHCP, налаштування `isc-dhcp-server`, defect report | [Lab03](Lab03/) |
| 4 | NAT за допомогою `iptables`, траблшутінг мережі, Test Plan і defect reports | [Lab04](Lab04/) |
| 5 | Протоколи TCP/UDP, iperf, тестування навантаження, Test Plan і defect reports | [Lab05](Lab05/) |
| 6 | Модель OSI, інкапсуляція, сеанси HTTP і FTP, Test Plan і defect reports | [Lab06](Lab06/) |
| 7 | Автоматизація тестів на Python: iperf, subprocess, pytest, paramiko, Test Plan і defect reports | [Lab07](Lab07/) |

## Структура

Кожна лабораторна лежить в окремій папці `LabNN/`:

```
LabNN/
  README.md      ← короткий опис і перелік файлів
  report.pdf     ← звіт
  screenshots/   ← скриншоти, використані у звіті
  configs/       ← конфігураційні файли (якщо є)
  captures/      ← захоплення трафіку .pcap (відкриваються у Wireshark)
  logs/          ← текстові виводи команд і журнали
  part1/, part2/ ← код на Python (Lab07)
```
