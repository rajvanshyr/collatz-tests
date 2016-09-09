"""
TestCollatz.py
"""
#!usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_max_range

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Test cases for Collatz.py
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
        testing collatz_read
        """
        stdin = "1 10\n"
        low, high = collatz_read(stdin)
        self.assertEqual(low, 1)
        self.assertEqual(high, 10)

    def test_read2(self):
        """
        testing collatz_read
        """
        stdin = "123123 999999\n"
        low, high = collatz_read(stdin)
        self.assertEqual(low, 123123)
        self.assertEqual(high, 999999)

    def test_read3(self):
        """
        testing collatz_read
        """
        stdin = "420420 420\n"
        low, high = collatz_read(stdin)
        self.assertEqual(low, 420420)
        self.assertEqual(high, 420)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        testing collatz_eval
        """
        var = collatz_eval(5, 100)
        self.assertEqual(var, 119)

    def test_eval_2(self):
        """
        testing collatz_eval
        """
        var = collatz_eval(900, 100)
        self.assertEqual(var, 179)

    def test_eval_3(self):
        """
        testing collatz_eval
        """
        var = collatz_eval(123, 321)
        self.assertEqual(var, 131)

    def test_eval_4(self):
        """
        testing collatz_eval
        """
        var = collatz_eval(1, 1000000)
        self.assertEqual(var, 525)

    # -----
    # max_range
    # -----

    def test_max_range_1(self):
        """
        testing collatz_max_range
        """
        var = collatz_max_range(1, 10)
        self.assertEqual(var, 20)

    def test_max_range_2(self):
        """
        testing collatz_max_range
        """
        var = collatz_max_range(1, 50)
        self.assertEqual(var, 112)

    def test_max_range_3(self):
        """
        testing collatz_max_range
        """
        var = collatz_max_range(1, 999)
        self.assertEqual(var, 179)

    # -----
    # print
    # -----

    def test_print(self):
        """
        testing collatz_print
        """
        write = StringIO()
        collatz_print(write, 1, 50, 100)
        self.assertEqual(write.getvalue(), "1 50 100\n")

    def test_print2(self):
        """
        testing collatz_print
        """
        write = StringIO()
        collatz_print(write, 1, 1, 1)
        self.assertEqual(write.getvalue(), "1 1 1\n")

    def test_print3(self):
        """
        testing collatz_print
        """
        write = StringIO()
        collatz_print(write, 1, 1000000, 525)
        self.assertEqual(write.getvalue(), "1 1000000 525\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        testing collatz_solve
        """
        read = StringIO("1 50\n555 32\n153 234\n1000 1\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 50 112\n555 32 144\n153 234 128\n1000 1 179\n")

    def test_solve2(self):
        """
        testing collatz_solve
        """
        read = StringIO("\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "")

    def test_solve3(self):
        """
        testing collatz_solve
        """
        read = StringIO("1 999\n1001 9999\n123 123123\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 999 179\n1001 9999 262\n123 123123 354\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
