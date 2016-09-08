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
    """Testing Collatz"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Testing read"""
        strg = "1 10\n"
        start, end = collatz_read(strg)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """Testing read"""
        strg = "3 4\n"
        start, end = collatz_read(strg)
        self.assertEqual(start, 3)
        self.assertEqual(end, 4)

    def test_read_3(self):
        """Testing read"""
        strg = "77 80\n"
        start, end = collatz_read(strg)
        self.assertEqual(start, 77)
        self.assertEqual(end, 80)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Testing eval"""
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """Testing eval"""
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """Testing eval"""
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """Testing eval"""
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        """Testing max cycle"""
        val = collatz_eval(418515, 603657)
        self.assertEqual(val, 470)

    def test_eval_6(self):
        """Testing max cycle"""
        val = collatz_eval(132501, 322152)
        self.assertEqual(val, 443)

    def test_eval_7(self):
        """Testing max cycle"""
        val = collatz_eval(241267, 283022)
        self.assertEqual(val, 407)

    def test_eval_8(self):
        """Testing max cycle"""
        val = collatz_eval(443846, 945884)
        self.assertEqual(val, 525)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Testing print"""
        inputoutput = StringIO()
        collatz_print(inputoutput, 1, 10, 20)
        self.assertEqual(inputoutput.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """Testing print"""
        inputoutput = StringIO()
        collatz_print(inputoutput, 2, 11, 21)
        self.assertEqual(inputoutput.getvalue(), "2 11 21\n")

    def test_print_3(self):
        """Testing print"""
        inputoutput = StringIO()
        collatz_print(inputoutput, 4, 5, 6)
        self.assertEqual(inputoutput.getvalue(), "4 5 6\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """Testing solve"""
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
