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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, naive_cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        line = "1 10\n"
        start, end = collatz_read(line)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        line = "10 1\n"
        start, end = collatz_read(line)
        self.assertEqual(start, 10)
        self.assertEqual(end, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        maxcycle = collatz_eval(1, 10)
        self.assertEqual(maxcycle, 20)

    def test_eval_2(self):
        maxcycle = collatz_eval(100, 200)
        self.assertEqual(maxcycle, 125)

    def test_eval_3(self):
        maxcycle = collatz_eval(201, 210)
        self.assertEqual(maxcycle, 89)

    def test_eval_4(self):
        maxcycle = collatz_eval(900, 1000)
        self.assertEqual(maxcycle, 174)

    def test_eval_5(self):
        maxcycle = collatz_eval(1, 1000000)
        self.assertEqual(maxcycle, 525)

    # -----
    # print
    # -----

    def test_print_1(self):
        out = StringIO()
        collatz_print(out, 1, 10, 20)
        self.assertEqual(out.getvalue(), "1 10 20\n")

    def test_print_2(self):
        out = StringIO()
        collatz_print(out, 10, 1000000, 525)
        self.assertEqual(out.getvalue(), "10 1000000 525\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        out = StringIO()
        collatz_solve(reader, out)
        self.assertEqual(
            out.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("1 1000000\n")
        out = StringIO()
        collatz_solve(reader, out)
        self.assertEqual(out.getvalue(), "1 1000000 525\n")

    def test_solve_3(self):
        reader = StringIO("100 200\n1 10\n1 1000000\n1 1\n")
        out = StringIO()
        collatz_solve(reader, out)
        self.assertEqual(
            out.getvalue(), "100 200 125\n1 10 20\n1 1000000 525\n1 1 1\n")

    def test_solve_4(self):
        reader = StringIO("100 1\n")
        out = StringIO()
        collatz_solve(reader, out)
        self.assertEqual(out.getvalue(), "100 1 119\n")

    # ------------
    # cycle length
    # ------------

    def test_cycle_length_1(self):
        cycle = cycle_length(10)
        self.assertEqual(cycle, 7)

    def test_cycle_length_2(self):
        cycle = cycle_length(1)
        self.assertEqual(cycle, 1)

    def test_cycle_length_3(self):
        cycle = cycle_length(1000000)
        self.assertEqual(cycle, 153)

    # ------------------
    # naive cycle length
    # ------------------

    def test_naive_cycle_length_1(self):
        cycle = naive_cycle_length(10)
        self.assertEqual(cycle, 7)

    def test_naive_cycle_length_2(self):
        cycle = naive_cycle_length(1)
        self.assertEqual(cycle, 1)

    def test_naive_cycle_length_3(self):
        cycle = naive_cycle_length(1000000)
        self.assertEqual(cycle, 153)

# ----
# main
# ----

if __name__ == "__main__":
    main()
