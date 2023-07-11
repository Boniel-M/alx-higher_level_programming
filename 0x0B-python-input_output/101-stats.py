#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import sys
from collections import defaultdict


def compute_metrics():
    """
    Read input from stdin, compute metrics, and print statistics.
    """
    file_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                parts = line.split()
                file_size += int(parts[-1])
                status_code = int(parts[-2])
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)


def print_statistics(file_size, status_codes):
    """
    Print the computed statistics.

    Args:
        file_size (int): Total file size.
        status_codes (dict): Number of lines by status code.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    compute_metrics()
