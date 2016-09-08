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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_eval_individual

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):

    # ----
    # read
    # ----

    def test_read(self):
        string_input = "1 10\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 1)
        self.assertEqual(second, 10)

    def test_read2(self):
        string_input = "100 106\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 100)
        self.assertEqual(second, 106)

    def test_read3(self):
        string_input = "1000 2000\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 1000)
        self.assertEqual(second, 2000)

    def test_read4(self):
        string_input = "5 3\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 5)
        self.assertEqual(second, 3)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        value = collatz_eval(11, 16)
        self.assertEqual(value, 18)

    def test_eval_6(self):
        value = collatz_eval(1, 1000)
        self.assertEqual(value, 179)

    def test_eval_7(self):
        value = collatz_eval(103, 269)
        self.assertEqual(value, 128)

    # -----
    # print
    # -----

    def test_print(self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2(self):
        w = StringIO()
        collatz_print(w, 111, 222, 125)
        self.assertEqual(w.getvalue(), "111 222 125\n")

    def test_print3(self):
        w = StringIO()
        collatz_print(w, 3048, 4125, 238)
        self.assertEqual(w.getvalue(), "3048 4125 238\n")

    def test_print4(self):
        w = StringIO()
        collatz_print(w, 1106, 2222, 182)
        self.assertEqual(w.getvalue(), "1106 2222 182\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        reader = StringIO("1 3\n132 164\n206 315\n400 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 3 8\n132 164 117\n206 315 131\n400 1000 179\n")

    def test_solve3(self):
        reader = StringIO("22 26\n1 31\n5 1032\n1113 2246\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "22 26 24\n1 31 112\n5 1032 179\n1113 2246 183\n")

    def test_solve4(self):
        reader = StringIO("106 2000\n37 189\n1337 2048\n916 917\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "106 2000 182\n37 189 125\n1337 2048 180\n916 917 37\n")

    # ---------------
    # eval_individual
    # ---------------

    def test_eval_individual(self):
        value = collatz_eval_individual(10)
        self.assertEqual(value, 7)

    def test_eval_individual2(self):
        value = collatz_eval_individual(5)
        self.assertEqual(value, 6)

    def test_eval_individual3(self):
        value = collatz_eval_individual(20)
        self.assertEqual(value, 8)

# ----
# main
# ----

if __name__ == "__main__":
    main()
