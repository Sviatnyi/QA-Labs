"""Тест пропускної здатності: Transfer > 2 МБайт і Bitrate > 20 Мбіт/с у кожному інтервалі."""
import os

import parser

MIN_TRANSFER = float(os.environ.get('MIN_TRANSFER', '2'))   # МБайт
MIN_BITRATE = float(os.environ.get('MIN_BITRATE', '20'))    # Мбіт/с


class TestSuite:

    def test_iperf_client_connection(self, client):
        """Клієнт не повертає помилку, а кожен інтервал iperf має Transfer і Bitrate більше порогу."""
        output, error = client
        assert not error, f'iperf client error: {error}'

        intervals = parser.parser(output)
        assert intervals, 'parser did not find any iperf intervals'

        for value in intervals:
            assert value['Transfer'] > MIN_TRANSFER, \
                f"{value['Interval']}: Transfer {value['Transfer']} MB <= {MIN_TRANSFER} MB"
            assert value['Bitrate'] > MIN_BITRATE, \
                f"{value['Interval']}: Bitrate {value['Bitrate']} Mbit/s <= {MIN_BITRATE} Mbit/s"
