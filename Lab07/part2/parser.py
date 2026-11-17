"""Парсер виводу iperf (iperf 2.x) на стороні клієнта."""
import re

# [  1] 0.0000-1.0000 sec   394 MBytes  3305 Mbits/sec   3152/0   12   1234K/456 us
REGEXP = re.compile(
    r'\[\s*\d+\]\s+(?P<start>\d+(?:\.\d+)?)\s*-\s*(?P<end>\d+(?:\.\d+)?)\s+sec\s+'
    r'(?P<transfer>\d+(?:\.\d+)?)\s+(?P<tunit>[KMG]?)Bytes\s+'
    r'(?P<bitrate>\d+(?:\.\d+)?)\s+(?P<bunit>[KMG]?)bits/sec'
    r'(?:\s+\d+/\d+\s+(?P<retr>\d+)\s+(?P<cwnd>\d+)K)?'
)
KEYS = ('Interval', 'Transfer', 'Bitrate', 'Retr', 'Cwnd')

# переведення в МБайти та Мбіт/с
BYTES = {'': 1 / 1024 ** 2, 'K': 1 / 1024, 'M': 1.0, 'G': 1024.0}
BITS = {'': 1e-6, 'K': 1e-3, 'M': 1.0, 'G': 1000.0}


def parser(output, interval=1.0):
    """Повертає список інтервалів iperf у вигляді словників.

    Приклад: {'Interval': '1.00-2.00', 'Transfer': 394.0, 'Bitrate': 3305.0, 'Retr': 0.0, 'Cwnd': 1234.0}
    Transfer – МБайт, Bitrate – Мбіт/с, Cwnd – КБайт.
    Підсумковий рядок (наприклад 0.00-10.00) не входить до списку.
    """
    result = []
    for m in REGEXP.finditer(output):
        start, end = float(m['start']), float(m['end'])
        if end - start > interval + 0.5:      # підсумок за весь тест
            continue
        result.append(dict(zip(KEYS, (
            f'{start:.2f}-{end:.2f}',
            round(float(m['transfer']) * BYTES[m['tunit']], 3),
            round(float(m['bitrate']) * BITS[m['bunit']], 3),
            float(m['retr']) if m['retr'] else 0.0,
            float(m['cwnd']) if m['cwnd'] else 0.0,
        ))))
    return result
