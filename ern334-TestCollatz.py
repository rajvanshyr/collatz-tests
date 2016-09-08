#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""Contains unit tests for the methods defined in Collatz.py"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import cycle_length, collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """Unit tests for each method in Collatz.py"""

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        """Calculate the cycle length of the special case, 1."""
        value = cycle_length(1)
        self.assertEqual(value, 1)

    def test_cycle_length_2(self):
        """Calculate the cycle length of an even number."""
        value = cycle_length(2)
        self.assertEqual(value, 2)

    def test_cycle_length_3(self):
        """Calculate the cycle length of an odd number."""
        value = cycle_length(3)
        self.assertEqual(value, 8)

    def test_cycle_length_4(self):
        """Calculate the cycle length of a power of 2."""
        value = cycle_length(16384)
        self.assertEqual(value, 15)

    def test_cycle_length_5(self):
        """Calculate the cycle length of an arbitrary number."""
        value = cycle_length(30011)
        self.assertEqual(value, 91)

    # ----
    # read
    # ----

    def test_read_1(self):
        """Read in a single pair of integers."""
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Evaluate the max cycle length over the entire range."""
        value = collatz_eval(1, 999999)
        self.assertEqual(value, 525)

    def test_eval_2(self):
        """Evaluate the max cycle length over the range (e//2 + 1, e) for an arbitrary e."""
        value = collatz_eval(101, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """Evaluate the max cycle length over the range (1, e) for an arbitrary e."""
        value = collatz_eval(1, 200)
        self.assertEqual(value, 125)

    def test_eval_4(self):
        """Evaluate the max cycle length over the range (e, 1) for some e greater than 1."""
        value = collatz_eval(210, 1)
        self.assertEqual(value, 125)

    def test_eval_5(self):
        """Evaluate the max cycle length over a range large enough to use the meta cache."""
        value = collatz_eval(123456, 234567)
        self.assertEqual(value, 443)

    def test_eval_6(self):
        """Evaluate the max cycle length over a large range unable to use the meta cache."""
        value = collatz_eval(5500, 6500)
        self.assertEqual(value, 262)

    # -----
    # print
    # -----
    def test_print(self):
        """Print out three numbers that could represent a line of output from the solver."""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """Solve the example input given by SPOJ."""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_extra_newline(self):
        """Solve bad input that has unnecessary newlines."""
        reader = StringIO("\n800000 999999\n\n600000 650000\n\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "800000 999999 525\n600000 650000 509\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
