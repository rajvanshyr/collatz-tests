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

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read_1(self):
        string = "1 10\n"
        minimum, maximum = collatz_read(string)
        self.assertEqual(minimum, 1)
        self.assertEqual(maximum, 10)

    def test_read_2(self):
        string = "50 50\n"
        minimum, maximum = collatz_read(string)
        self.assertEqual(minimum, 50)
        self.assertEqual(maximum, 50)

    def test_read_3(self):
        string = "123 20\n"
        minimum, maximum = collatz_read(string)
        self.assertEqual(minimum, 123)
        self.assertEqual(maximum, 20)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        evald = collatz_eval(1, 10)
        self.assertEqual(evald, 20)

    def test_eval_2(self):
        evald = collatz_eval(100, 200)
        self.assertEqual(evald, 125)

    def test_eval_3(self):
        evald = collatz_eval(201, 210)
        self.assertEqual(evald, 89)

    def test_eval_4(self):
        evald = collatz_eval(900, 1000)
        self.assertEqual(evald, 174)

    def test_eval_5(self):
        evald = collatz_eval(12345, 3)
        self.assertEqual(evald, 268)

    def test_eval_6(self):
        METACACHE = "10001 10500 255"
        evald = collatz_eval(10001, 10500)
        self.assertEqual(evald, 255)

    # -----
    # print
    # -----

    def test_print_1(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        writer = StringIO()
        collatz_print(writer, 1500, 3000, 217)
        self.assertEqual(writer.getvalue(), "1500 3000 217\n")

    def test_print_3(self):
        writer = StringIO()
        collatz_print(writer, 10000, 20, 262)
        self.assertEqual(writer.getvalue(), "10000 20 262\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        reader = StringIO("20 800\n999999 1\n999998 54321\n975648 170384\n643784 643788\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "20 800 171\n999999 1 525\n999998 54321 525\n975648 170384 525\n643784 643788 155\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
