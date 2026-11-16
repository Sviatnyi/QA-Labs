# Лабораторна робота №4. NAT, iptables, траблшутінг

**Виконав:** Святний Тимофій, група ІО-34

- [`report.pdf`](report.pdf) — звіт (Test Plan TP-NAT-01, тест-кейси TC-NAT-01…03, defect reports DEF-NAT-01/02)
- [`screenshots/`](screenshots/) — скриншоти до звіту
- [`configs/`](configs/) — `iptables.rules` (збережені правила NAT), `dhcpd.conf`
- [`captures/`](captures/) — захоплення ICMP `.pcap` на внутрішньому (`enp0s8`) і зовнішньому (`enp0s3`) інтерфейсах: з NAT, без NAT, інцидент
- [`logs/`](logs/) — вивід клієнта, розшифровки захоплень, лічильники iptables, журнал NetworkManager
