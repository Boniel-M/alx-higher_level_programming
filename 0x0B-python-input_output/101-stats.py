#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import sys
from collections import defaultdict


def print_statistics(file_size, status_codes):
    """
    Print the computed statistics.

    Args:
        file_size (int): Total file size.
        status_codes (dict): Number of lines by status code.
    """
    print("File size:", file_size)
    for status_code in sorted(status_codes.keys()):
        count = status_codes[status_code]
        print(f"{status_code}: {count}")


def parse_line(line):
    """
    Parse a line and extract file size and status code.

    Args:
        line (str): The line to parse.

    Returns:
        tuple: The file size and status code.
    """
    parts = line.split()
    file_size = int(parts[-1])
    status_code = int(parts[-2])
    return file_size, status_code


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
                file_size_delta, status_code = parse_line(line)
                file_size += file_size_delta
                status_codes[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print_statistics(file_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
