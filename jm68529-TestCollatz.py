#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright(C) 2016
# Glenn P. Downing
# -------------------------------
"""Tests all the functions in Collatz.py"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, eval_helper

# -----------
# TestCollatz
# -----------

# pylint: disable=R0904
class TestCollatz(TestCase):
    """Testing class for Collatz"""
    # ----
    # read
    # ----

    def test_read1(self):
        string = "1 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read2(self):
        string = "-1 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, -1)
        self.assertEqual(end, 10)

    def test_read3(self):
        string = "10 1\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 10)
        self.assertEqual(end, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    def test_eval_5(self):
        result = collatz_eval(1000, 1000)
        self.assertEqual(result, 112)

    def test_eval_6(self):
        result = collatz_eval(1500, 4500)
        self.assertEqual(result, 238)

    def test_eval_7(self):
        result = collatz_eval(1500, 1800)
        self.assertEqual(result, 180)

    def test_eval_8(self):
        result = collatz_eval(2000, 5500)
        self.assertEqual(result, 238)

    def test_eval_9(self):
        result = collatz_eval(2500, 5000)
        self.assertEqual(result, 238)

    def test_eval_10(self):
        result = collatz_eval(3000, 5000)
        self.assertEqual(result, 238)
    # -----
    # print
    # -----

    def test_print1(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print2(self):
        writer = StringIO()
        collatz_print(writer, 10, 1, 20)
        self.assertEqual(writer.getvalue(), "10 1 20\n")

    def test_print3(self):
        writer = StringIO()
        collatz_print(writer, 100, 200, 126)
        self.assertEqual(writer.getvalue(), "100 200 126\n")

    # -----
    # solve
    # -----

    def test_solve1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        reader = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve3(self):
        reader = StringIO("1 10\n100 200\n0 210\n900 1000\n")
        writer = StringIO()
        self.assertRaises(AssertionError, collatz_solve, reader, writer)

    def test_solve4(self):
        reader = StringIO("1 10\n\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    # ----------------
    # get cycle length
    # ----------------

    def test_cycle_length1(self):
        self.assertEqual(cycle_length(1), 1)

    def test_cycle_length2(self):
        self.assertEqual(cycle_length(1500), 48)

    def test_cycle_length3(self):
        self.assertRaises(AssertionError, cycle_length, 0)

    # -------------------
    # collatz eval helper
    # -------------------
    def test_eval_helper1(self):
        self.assertEqual(eval_helper(1, 100), 119)

    def test_eval_helper2(self):
        self.assertRaises(AssertionError, eval_helper, 3, 1)

    def test_eval_helper3(self):
        self.assertEqual(eval_helper(6, 7), 17)

# ----
# main
# ----

if __name__ == "__main__":
    main()
