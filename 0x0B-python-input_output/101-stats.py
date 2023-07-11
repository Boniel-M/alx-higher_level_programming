#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""


import sys
from collections import defaultdict

# Initialize variables
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
                print(f"File size: {file_size}")
                for code in sorted(status_codes.keys()):
                    if status_codes[code] > 0:
                        print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
