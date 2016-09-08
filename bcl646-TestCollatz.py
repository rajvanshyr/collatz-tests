#!/usr/bin/env python3
"""
Tests for Collatz.py.
"""

# pylint: disable=missing-docstring, invalid-name

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycles

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "99999 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 99999)
        self.assertEqual(j, 999999)

    def test_read_3(self):
        s = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    # ------
    # cycles
    # ------

    def test_cycles_1(self):
        i = collatz_cycles(1)
        self.assertEqual(i, 1)

    def test_cycles_2(self):
        i = collatz_cycles(10)
        self.assertEqual(i, 7)

    def test_cycles_3(self):
        i = collatz_cycles(999999)
        self.assertEqual(i, 259)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2(self):
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3(self):
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4(self):
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6(self):
        v = collatz_eval(1, 99999)
        self.assertEqual(v, 351)

    # -----
    # print
    # -----

    def test_print_1(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 111111, 222222, 333333)
        self.assertEqual(w.getvalue(), "111111 222222 333333\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_solve_2(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        r = StringIO("")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()
