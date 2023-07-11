#!/usr/bin/python3

"""
a script that reads stdin line by line and computes metrics
"""

import sys
import signal
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0


def keyboard_interrupt_handler(signal, frame):
    """Handler for keyboard interruption (CTRL+C).
    """
    print_statistics()
    sys.exit(0)


def print_statistics():
    """Prints the accumulated metrics.
    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_code_counts):
        count = status_code_counts[status_code]
        print("{}: {}".format(status_code, count))


# Register the keyboard interruption handler
signal.signal(signal.SIGINT, keyboard_interrupt_handler)

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        # Parse the input line
        parts = line.split()
        if len(parts) != 7:
            continue

        status_code = parts[5]
        file_size = int(parts[6])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        line_count += 1

        # Check if it's time to print statistics
        if line_count % 10 == 0:
            print_statistics()

    # Print the final statistics
    print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise
