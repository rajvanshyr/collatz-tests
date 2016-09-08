#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Contains unit tests for Collatz.py
"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Contains unit tests for Collatz.py functions
    """

    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Tests collatz_read to make sure it gives correct range
        for "1 10\n"
        """
        line = "1 10\n"
        range_start, range_end = collatz_read(line)
        self.assertEqual(range_start, 1)
        self.assertEqual(range_end, 10)

    def test_read_2(self):
        """
        Tests collatz_read to make sure it gives correct range
        for " 1 2 \n"
        """
        line = " 1 2 \n"
        range_start, range_end = collatz_read(line)
        self.assertEqual(range_start, 1)
        self.assertEqual(range_end, 2)

    def test_read_3(self):
        """
        Tests collatz_read to make sure it gives correct range
        for "1 1\n"
        """
        line = "1 1\n"
        range_start, range_end = collatz_read(line)
        self.assertEqual(range_start, 1)
        self.assertEqual(range_end, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Tests collatz_eval to see if it gives
        correct max_cycle_length for (1, 10)
        """
        max_cycle_length = collatz_eval(1, 10)
        self.assertEqual(max_cycle_length, 20)

    def test_eval_2(self):
        """
        Tests collatz_eval to see if it gives
        correct max_cycle_length for (100, 200)
        """
        max_cycle_length = collatz_eval(100, 200)
        self.assertEqual(max_cycle_length, 125)

    def test_eval_3(self):
        """
        Tests collatz_eval to see if it gives
        correct max_cycle_length for (201, 210)
        """
        max_cycle_length = collatz_eval(201, 210)
        self.assertEqual(max_cycle_length, 89)

    def test_eval_4(self):
        """
        Tests collatz_eval to see if it gives
        correct max_cycle_length for (900, 1000)
        """
        max_cycle_length = collatz_eval(900, 1000)
        self.assertEqual(max_cycle_length, 174)

    def test_eval_5(self):
        """
        Tests collatz_eval to see if it gives
        correct max_cycle_length for (5, 5)
        """
        max_cycle_length = collatz_eval(5, 5)
        self.assertEqual(max_cycle_length, 6)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Tests collatz_print to make sure the writing
        is performed and formatted correctly
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Tests collatz_print to make sure the writing
        is performed and formatted correctly
        """
        writer = StringIO()
        collatz_print(writer, 1, 1, 1)
        self.assertEqual(writer.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Tests collatz_solve to see if the correct
        max_cycle_lengths are computed for each range and
        all of the writes are formatted correctly
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        Tests collatz_solve to see if it will skip over whitespace lines
        """
        reader = StringIO("1 10\n  \n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        """
        Tests collatz_solve to see if it will form the correct range given i, j
        """
        reader = StringIO("10 1")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
