#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# pylint: disable=missing-docstring,too-many-public-methods

"""
Runs tests on Collatz.py
"""

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, cycle_length, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    # ----
    # read
    # ----

    def test_read(self):
        string = "1 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        string = "999999 999999\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 999999)
        self.assertEqual(end, 999999)

    def test_read_3(self):
        string = "9999 10\n"
        begin, end = collatz_read(string)
        self.assertEqual(begin, 9999)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        c_length = collatz_eval(1, 10)
        self.assertEqual(c_length, 20)

    def test_eval_2(self):
        c_length = collatz_eval(100, 200)
        self.assertEqual(c_length, 125)

    def test_eval_3(self):
        c_length = collatz_eval(201, 210)
        self.assertEqual(c_length, 89)

    def test_eval_4(self):
        c_length = collatz_eval(900, 1000)
        self.assertEqual(c_length, 174)

    def test_eval_5(self):
        c_length = collatz_eval(1, 999999)
        self.assertEqual(c_length, 525)

    def test_eval_6(self):
        c_length = collatz_eval(1, 1)
        self.assertEqual(c_length, 1)

    def test_eval_7(self):
        c_length = collatz_eval(1, 837799)
        self.assertEqual(c_length, 525)

    # -------------
    # cycle_length
    # -------------
    def test_cycle_1(self):
        c_length = cycle_length(1)
        self.assertEqual(c_length, 1)

    def test_cycle_2(self):
        c_length = cycle_length(999999)
        self.assertEqual(c_length, 259)

    def test_cycle_3(self):
        c_length = cycle_length(837799)
        self.assertEqual(c_length, 525)

    # -----
    # print
    # -----
    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_big(self):
        writer = StringIO()
        collatz_print(writer, 999999, 999999, 999999)
        self.assertEqual(writer.getvalue(), "999999 999999 999999\n")

    def test_print_zero(self):
        writer = StringIO()
        collatz_print(writer, 0, 0, 0)
        self.assertEqual(writer.getvalue(), "0 0 0\n")

    # -----
    # solve
    # -----
    def test_solve(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n"
            + "201 210 89\n900 1000 174\n")

    def test_solve_same(self):
        reader = StringIO(
            "1 1\n100 100\n2000 2000\n90000 90000\n999999 999999\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 1 1\n100 100 26\n"
            + "2000 2000 113\n90000 90000 165\n999999 999999 259\n")

    def test_solve_backwards(self):
        reader = StringIO("10 1\n200 100\n210 201\n1000 900\n999999 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n200 100 125\n"
            + "210 201 89\n1000 900 174\n999999 1 525\n")

    def test_solve_empty(self):
        reader = StringIO("10 1\n\n10 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n10 1 20\n")
# ----
# main
# ----

if __name__ == "__main__":
    main()
