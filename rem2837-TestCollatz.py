#!/usr/bin/env python3
"""
File to test Collatz.py
"""

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
    # pylint: disable=C0111
    # ----
    # read
    # ----

    def test_read_1(self):
        """test normal input"""
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """test input with one extra space"""
        start, end = collatz_read("100  300\n")
        self.assertEqual(start, 100)
        self.assertEqual(end, 300)

    def test_read_3(self):
        """test input with multiple extra spaces"""
        start, end = collatz_read("1     5000\n")
        self.assertEqual(start, 1)
        self.assertEqual(end, 5000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """test 1 to 10"""
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """test 100 to 200"""
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        """test range of only 1"""
        val = collatz_eval(10000, 10001)
        self.assertEqual(val, 180)

    def test_eval_6(self):
        """test 0 to 1"""
        val = collatz_eval(1, 2)
        self.assertEqual(val, 2)

    def test_eval_7(self):
        val = collatz_eval(1, 10000)
        self.assertEqual(val, 262)

    def test_eval_8(self):
        val = collatz_eval(8, 64)
        self.assertEqual(val, 113)

    def test_eval_9(self):
        val = collatz_eval(1000, 6000)
        self.assertEqual(val, 238)

    def test_eval_10(self):
        val = collatz_eval(7250, 10540)
        self.assertEqual(val, 260)

    def test_eval_11(self):
        """test 123 to 456"""
        val = collatz_eval(123, 456)
        self.assertEqual(val, 144)

    def test_eval_12(self):
        """test 123124 to 129384"""
        val = collatz_eval(123124, 129384)
        self.assertEqual(val, 331)

    def test_eval_13(self):
        """test 1 to 500"""
        val = collatz_eval(1, 500)
        self.assertEqual(val, 144)

    def test_eval_14(self):
        """test 2 to 2000"""
        val = collatz_eval(2, 2000)
        self.assertEqual(val, 182)

    def test_eval_15(self):
        """testing range of a single number"""
        val = collatz_eval(12, 12)
        self.assertEqual(val, 10)


    # -----
    # print
    # -----

    def test_print(self):
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n 10 1\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n10 1 20\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
