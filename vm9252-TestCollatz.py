#!/usr/bin/env python3
"""
Unit tests for the Collatz module
"""

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    contains tests for Collatz
    """
    # ----
    # read
    # ----

    def test_read(self):
        """Tests collatz_read function"""
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)


    # ----
    # cycle_lengths
    # ----

    def test_cycle_lengths_1(self):
        """tests collatz_cycle_length with base case"""
        value = collatz_cycle_length(1)
        self.assertEqual(value, 1)

    def test_cycle_lengths_2(self):
        """tests collatz_cycle_length with largest given input"""
        value = collatz_cycle_length(1000000)
        self.assertEqual(value, 153)

    def test_cycle_lengths_3(self):
        """tests collatz_cycle_length with number whose cycle contains the largest number reached"""
        value = collatz_cycle_length(511935)
        self.assertEqual(value, 470)

    def test_cycle_lengths_4(self):
        """tests collatz_cycle_length with number with longest cycle"""
        value = collatz_cycle_length(837799)
        self.assertEqual(value, 525)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """tests collatz_eval on given range"""
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """tests collatz_eval on given range"""
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """tests collatz_eval on given range"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """tests collatz_eval on given range"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """tests collatz_eval on largest possible range"""
        value = collatz_eval(1, 1000000)
        self.assertEqual(value, 525)

    def test_eval_6(self):
        """tests collatz_eval with range containing largest number and longest cycle"""
        value = collatz_eval(511935, 837799)
        self.assertEqual(value, 525)

    def test_eval_7(self):
        """tests collatz_eval on reversed input"""
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)


    # -----
    # print
    # -----

    def test_print(self):
        """tests collatz_print"""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """tests collatz_solve"""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
