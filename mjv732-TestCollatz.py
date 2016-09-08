#!/usr/bin/env python3

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, round_num, eval_current

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ---------
    # round_num
    # ---------

    def test_round_num_1(self):
        n = 304
        r = round_num(n, True, 500)
        self.assertEqual(r, 500)

    def test_round_num_2(self):
        n = 1322
        r = round_num(n, False, 1000)
        self.assertEqual(r, 1000)

    def test_round_num_3(self):
        n = 10212
        r = round_num(n, False, 100000)
        self.assertEqual(r, 0)

    def test_round_num_4(self):
        n = 10212
        r = round_num(n, True, 100000)
        self.assertEqual(r, 100000)

    def test_round_num_5(self):
        n = 1000
        r = round_num(n, False, 1000)
        self.assertEqual(r, 1000)

    # ----
    # read
    # ----

    def test_read_1(self):
        s = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        s = "\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -1)

    # ------------
    # eval_current
    # ------------

    def test_eval_current_1(self):
        n = eval_current(8)
        self.assertEqual(n, 4)

    def test_eval_current_2(self):
        n = eval_current(5)
        self.assertEqual(n, 6)

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
        v = collatz_eval(500, 2500)
        self.assertEqual(v, 209)

    def test_eval_6(self):
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174")

    def test_solve_2(self):
        r = StringIO("1 10\n200 100\n\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(
            w.getvalue(), "1 10 20\n200 100 125\n201 210 89\n900 1000 174")

# ----
# main
# ----

if __name__ == "__main__":
    main()
