#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""When run as __main__ Collatz test cases are checked"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve


class TestCollatz(TestCase):
    """Evaluate test cases on every function of Collatz"""

    # ----
    # read
    # ----

    def test_read_0(self):
        line = "1 10\n"
        first, second = collatz_read(line)
        self.assertEqual(first, 1)
        self.assertEqual(second, 10)

    def test_read_1(self):
        line = "1000000 1\n"
        first, second = collatz_read(line)
        self.assertEqual(first, 1000000)
        self.assertEqual(second, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        cycle_length = collatz_eval(1, 10)
        self.assertEqual(cycle_length, 20)

    def test_eval_2(self):
        cycle_length = collatz_eval(100, 200)
        self.assertEqual(cycle_length, 125)

    def test_eval_3(self):
        cycle_length = collatz_eval(201, 210)
        self.assertEqual(cycle_length, 89)

    def test_eval_4(self):
        cycle_length = collatz_eval(900, 1000)
        self.assertEqual(cycle_length, 174)

    def test_eval_5(self):
        cycle_length = collatz_eval(10, 1)
        self.assertEqual(cycle_length, 20)

    def test_eval_6(self):
        cycle_length = collatz_eval(2000, 200000)
        self.assertEqual(cycle_length, 383)

    # -----
    # print
    # -----

    def test_print(self):
        out = StringIO()
        collatz_print(out, 1, 10, 20)
        self.assertEqual(out.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("1 10\n100 200\n     \n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
