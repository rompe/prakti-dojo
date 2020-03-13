#!/usr/bin/env python
"""Unit tests for sum_all_numbers.py."""
import unittest

import sum_all_numbers


class SumAllNumbersTests(unittest.TestCase):
    """Tests for sum_all_numbers.py."""

    def test_sum_all_numbers(self):
        """Test sum_all_numbers()."""
        result = sum_all_numbers.sum_all_numbers(("1", "7", "und", "6"))
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
