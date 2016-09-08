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
        strg = "1 10\n"
        start, end = collatz_read(strg)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    # ---------------
    # more unit tests
    # ---------------

    def test_eval_5(self):
        val = collatz_eval(11, 1)
        self.assertEqual(val, 20)

    def test_eval_6(self):
        val = collatz_eval(350, 450)
        self.assertEqual(val, 134)

    def test_eval_7(self):
        val = collatz_eval(1, 3)
        self.assertEqual(val, 8)

    def test_eval_8(self):
        val = collatz_eval(200, 2300)
        self.assertEqual(val, 183)

    def test_eval_9(self):
        val = collatz_eval(88, 89)
        self.assertEqual(val, 31)

    def test_eval_10(self):
        val = collatz_eval(123, 456)
        self.assertEqual(val, 144)

    def test_eval_11(self):
        val = collatz_eval(45, 60)
        self.assertEqual(val, 113)

    def test_eval_12(self):
        val = collatz_eval(1, 999)
        self.assertEqual(val, 179)

    def test_eval_13(self):
        val = collatz_eval(1000, 1099)
        self.assertEqual(val, 169)

    def test_eval_14(self):
        val = collatz_eval(8889, 9000)
        self.assertEqual(val, 247)

    def test_eval_15(self):
        val = collatz_eval(42, 69)
        self.assertEqual(val, 113)

    def test_eval_16(self):
        val = collatz_eval(3, 3)
        self.assertEqual(val, 8)

    def test_eval_17(self):
        val = collatz_eval(123456, 123457)
        self.assertEqual(val, 88)

    def test_eval_18(self):
        val = collatz_eval(1050, 1350)
        self.assertEqual(val, 182)

    def test_eval_19(self):
        val = collatz_eval(999, 1001)
        self.assertEqual(val, 143)

    def test_eval_20(self):
        val = collatz_eval(1, 1)
        self.assertEqual(val, 1)

    # -----
    # print
    # -----

    def test_print(self):
        inputoutput = StringIO()
        collatz_print(inputoutput, 1, 10, 20)
        self.assertEqual(inputoutput.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
