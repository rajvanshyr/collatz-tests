#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Tester program for Collatz Conjecture
"""

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    A class to test functions from Collatz program
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        A function to test collatz_read.
        """
        string = "1 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """
        A function to test collatz_read.
        """
        string = "5 5\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 5)
        self.assertEqual(end, 5)

    def test_read_3(self):
        """
        A function to test collatz_read.
        """
        string = "125 120\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 125)
        self.assertEqual(end, 120)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        """
        A function to test cycle_length.
        """
        length = cycle_length(27)
        self.assertEqual(length, 112)

    def test_cycle_length_2(self):
        """
        A function to test cycle_length.
        """
        length = cycle_length(22221)
        self.assertEqual(length, 132)

    def test_cycle_length_3(self):
        """
        A function to test cycle_length.
        """
        length = cycle_length(9823)
        self.assertEqual(length, 123)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(100, 100)
        self.assertEqual(val, 26)

    def test_eval_6(self):
        """
        A function to test collatz_eval.
        """
        val = collatz_eval(206, 200)
        self.assertEqual(val, 89)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        A function to test collatz_print.
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        A function to test collatz_print.
        """
        writer = StringIO()
        collatz_print(writer, 5, 5, 6)
        self.assertEqual(writer.getvalue(), "5 5 6\n")

    def test_print_3(self):
        """
        A function to test collatz_print.
        """
        writer = StringIO()
        collatz_print(writer, 125, 10, 30)
        self.assertEqual(writer.getvalue(), "125 10 30\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        A function to test collatz_solve.
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        A function to test collatz_solve.
        """
        reader = StringIO("5 5\n125 120\n1 1\n55764 64444\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "5 5 6\n125 120 109\n1 1 1\n55764 64444 335\n")

    def test_solve_3(self):
        """
        A function to test collatz_solve.
        """
        reader = StringIO("4 15\n399 406\n997 1010\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "4 15 20\n399 406 121\n997 1010 143\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
