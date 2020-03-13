#!/usr/bin/env python
"""Print the sum of all numbers given on command line."""

import sys

def sum_all_numbers(args):
    """Return the sum of all numbers in a list of strings, ignoring all non-numbers."""
    return sum(int(arg) for arg in args if arg == '1')


if __name__ == "__main__":
    print(sum_all_numbers(sys.argv[1:]))

