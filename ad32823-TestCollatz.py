#!/usr/bin/env python3
"""
docstring
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, eval_helper

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    docstring
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        docstring
        """
        temp1 = "70 70000\n"
        temp2, temp3 = collatz_read(temp1)
        self.assertEqual(temp2, 70)
        self.assertEqual(temp3, 70000)

    def test_read_2(self):
        """
        docstring
        """
        temp1 = "1234 95685\n"
        temp2, temp3 = collatz_read(temp1)
        self.assertEqual(temp2, 1234)
        self.assertEqual(temp3, 95685)
    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        docstring
        """
        temp = collatz_eval(796489, 910767)
        self.assertEqual(temp, 525)

    def test_eval_2(self):
        """
        docstring
        """
        temp = collatz_eval(85371, 230974)
        self.assertEqual(temp, 443)

    def test_eval_3(self):
        """
        docstring
        """
        temp = collatz_eval(185217, 663797)
        self.assertEqual(temp, 509)

    def test_eval_4(self):
        """
        docstring
        """
        temp = collatz_eval(100, 100)
        self.assertEqual(temp, 26)

    def test_eval_5(self):
        """
        docstring
        """
        temp = collatz_eval(1, 1000000)
        self.assertEqual(temp, 525)

    # -----
    # helper
    # -----
    def test_helper_1(self):
        """
        docstring
        """
        temp = eval_helper(1)
        self.assertEqual(temp, 1)

    def test_helper_2(self):
        """
        docstring
        """
        temp = eval_helper(3)
        self.assertEqual(temp, 8)

    def test_helper_3(self):
        """
        docstring
        """
        temp = eval_helper(500)
        self.assertEqual(temp, 111)

    def test_helper_4(self):
        """
        docstring
        """
        temp = eval_helper(1000)
        self.assertEqual(temp, 112)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        docstring
        """
        temp1 = StringIO()
        collatz_print(temp1, 1234, 1234, 133)
        self.assertEqual(temp1.getvalue(), "1234 1234 133\n")

    def test_print_2(self):
        """
        docstring
        """
        temp1 = StringIO()
        collatz_print(temp1, 1, 1, 1)
        self.assertEqual(temp1.getvalue(), "1 1 1\n")

    def test_print_3(self):
        """
        docstring
        """
        temp1 = StringIO()
        collatz_print(temp1, 666, 666, 114)
        self.assertEqual(temp1.getvalue(), "666 666 114\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        docstring
        """
        read = StringIO("796489 910767\n85371 230974\n663797 185217\n140945 399307\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "796489 910767 525\n85371 230974 443\n663797 185217 509\n140945 399307 443\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
