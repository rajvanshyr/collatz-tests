#!/usr/bin/env python3

"""Unit Tests - White Box Testing for Collatz"""

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Unit Tests for Collatz.py functions/methods
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Tests that the inputs are read from each line
        """
        line = "1 10\n"
        first, second = collatz_read(line)
        self.assertEqual(first, 1)
        self.assertEqual(second, 10)

    def test_read_2(self):
        """
        Tests that the input can be read with first > second
        """
        line = "999999 1\n"
        first, second = collatz_read(line)
        self.assertEqual(first, 999999)
        self.assertEqual(second, 1)

    def test_read_3(self):
        """
        Tests that the inputs are read from each line
        """
        line = "100 50000\n"
        first, second = collatz_read(line)
        self.assertEqual(first, 100)
        self.assertEqual(second, 50000)

    def test_read_4(self):
        """
        Tests that the inputs are read from each line
        """
        reader = StringIO("9 70060\n")
        for item in reader:
            first, second = collatz_read(item)
        self.assertEqual(first, 9)
        self.assertEqual(second, 70060)

    def test_read_5(self):
        """
        Tests that multiple lines of the input are read.
        """
        reader = StringIO("700 3\n500 2\n")
        for item in reader:
            first, second = collatz_read(item)
        self.assertEqual(first, 500)
        self.assertEqual(second, 2)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Tests for max cycle between 1 - 10
        """
        maxc = collatz_eval(1, 10)
        self.assertEqual(maxc, 20)

    def test_eval_2(self):
        """
        Tests for max cycle between 100 - 200
        """
        maxc = collatz_eval(100, 200)
        self.assertEqual(maxc, 125)

    def test_eval_3(self):
        """
        Tests for max cycle between 201 - 210
        """
        maxc = collatz_eval(201, 210)
        self.assertEqual(maxc, 89)

    def test_eval_4(self):
        """
        Tests for max cycle between 900 - 1000
        """
        maxc = collatz_eval(900, 1000)
        self.assertEqual(maxc, 174)

    def test_eval_5(self):
        """
        Tests for max cycle between 1000 - 899
        """
        maxc = collatz_eval(1000, 899)
        self.assertEqual(maxc, 174)

    def test_eval_6(self):
        """
        Tests for max cycle between 501 - 2
        """
        maxc = collatz_eval(501, 2)
        self.assertEqual(maxc, 144)

    def test_eval_7(self):
        """
        Tests for max cycle multiple times
        """
        maxc = collatz_eval(501, 2)
        maxc = collatz_eval(1, 2)
        maxc = collatz_eval(1, 1)
        maxc = collatz_eval(6, 2)
        self.assertEqual(maxc, 9)

    def test_eval_8(self):
        """
        Tests for max cycle between 1001 - 2000
        """
        maxc = collatz_eval(1001, 2000)
        self.assertEqual(maxc, 182)

    def test_eval_9(self):
        """
        Tests for max cycle between 1000 2000
        """
        maxc = collatz_eval(1000, 2000)
        self.assertEqual(maxc, 182)

    def test_eval_10(self):
        """
        Tests for max cycle between 1000 - 5000
        """
        maxc = collatz_eval(1000, 5000)
        self.assertEqual(maxc, 238)

    def test_eval_11(self):
        """
        Tests for max cycle between 1001 - 5001
        """
        maxc = collatz_eval(1001, 5001)
        self.assertEqual(maxc, 238)

    def test_eval_12(self):
        """
        Tests for max cycle between 5001 - 1001
        """
        maxc = collatz_eval(5001, 1001)
        self.assertEqual(maxc, 238)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Tests printing to output source.
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Tests for multiple max cycle evals.
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        """
        Tests for multiple max cycle evals triggering the meta cache.
        """
        reader = StringIO("10 1\n2000 1000\n1000 2000\n1001 5001\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "10 1 20\n2000 1000 182\n1000 2000 182\n1001 5001 238\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
