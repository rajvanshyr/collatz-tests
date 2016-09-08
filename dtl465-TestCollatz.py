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

    def test_read(self):
        s_string = "1 10\n"
        begin, end = collatz_read(s_string)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

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
        value = collatz_eval(100, 400)
        self.assertEqual(value, 144)

    def test_eval_6(self):
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    def test_eval_7(self):
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    def test_eval_8(self):
        value = collatz_eval(40, 40)
        self.assertEqual(value, 9)

    def test_eval_9(self):
        value = collatz_eval(99999, 100000)
        self.assertEqual(value, 227)

    def test_eval_10(self):
        value = collatz_eval(100000, 100001)
        self.assertEqual(value, 129)

    def test_eval_11(self):
        value = collatz_eval(100500, 101000)
        self.assertEqual(value, 266)

    def test_eval_12(self):
        value = collatz_eval(100500, 110000)
        self.assertEqual(value, 354)

    def test_eval_13(self):
        value = collatz_eval(100500, 105000)
        self.assertEqual(value, 310)

    def test_eval_14(self):
        value = collatz_eval(75268, 73604)
        self.assertEqual(value, 325)

    def test_eval_15(self):
        value = collatz_eval(150837, 160000)
        self.assertEqual(value, 383)

    def test_eval_16(self):
        value = collatz_eval(61799, 55060)
        self.assertEqual(value, 335)

    def test_eval_17(self):
        value = collatz_eval(297198, 298655)
        self.assertEqual(value, 327)

    def test_eval_18(self):
        value = collatz_eval(5055, 1053)
        self.assertEqual(value, 238)

    def test_eval_19(self):
        value = collatz_eval(12345, 54321)
        self.assertEqual(value, 340)

    def test_eval_20(self):
        value = collatz_eval(7890, 9876)
        self.assertEqual(value, 260)

    def test_eval_21(self):
        value = collatz_eval(4567, 14000)
        self.assertEqual(value, 276)

    def test_eval_22(self):
        value = collatz_eval(42489, 31359)
        self.assertEqual(value, 324)

    # -----
    # print
    # -----

    def test_print(self):
        w_writer = StringIO()
        collatz_print(w_writer, 1, 10, 20)
        self.assertEqual(w_writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        r_reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w_writer = StringIO()
        collatz_solve(r_reader, w_writer)
        self.assertEqual(w_writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
