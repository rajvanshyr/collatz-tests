#!/usr/bin/env python3
#pylint: disable=missing-docstring, invalid-name

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------
"""
Tests all methods included in Collatz.py
"""

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_max_meta

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    """
    Tests all methods included in Collatz.py
    """

    def test_read(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)
    def test_read_2(self):
        s = "7337 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 7337)
        self.assertEqual(j, 10)
    def test_read_3(self):
        s = "123 234\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 123)
        self.assertEqual(j, 234)

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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    def test_eval_6(self):
        v = collatz_eval(5, 6)
        self.assertEqual(v, 9)

    def test_eval_7(self):
        v = collatz_eval(200, 601)
        self.assertEqual(v, 144)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    def test_print_2(self):
        w = StringIO()
        collatz_print(w, 18, 506139, 449)
        self.assertEqual(w.getvalue(), "18 506139 449\n")
    def test_print_3(self):
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n1000 900\n5 6\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1000 900 174\n5 6 9\n")

    def test_solve2(self):
        r = StringIO("181883 1289\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "181883 1289 383\n")

    def test_solve3(self):
        r = StringIO("200 601\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "200 601 144\n")

    def test_solve4(self):
        r = StringIO("        ")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    # -----
    # get_max_meta
    # -----

    def test_get_max_meta_1(self):
        v = get_max_meta(201, 600)
        self.assertEqual(v, 144)

    def test_get_max_meta_2(self):
        v = get_max_meta(201, 1000)
        self.assertEqual(v, 179)
    def test_get_max_meta_3(self):
        v = get_max_meta(1000, 201)
        self.assertEqual(v, 179)

# ----
# main
# ----

if __name__ == "__main__":
    main()
