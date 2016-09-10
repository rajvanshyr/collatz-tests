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
"""
docstring
"""

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----
    """
    docstring
    """

    def test_read(self):
        """
        docstring
        """
        svar = "1 10\n"
        ivar, jvar = collatz_read(svar)
        self.assertEqual(ivar, 1)
        self.assertEqual(jvar, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        docstring
        """
        vvar = collatz_eval(1, 10)
        self.assertEqual(vvar, 20)

    def test_eval_2(self):
        """
        docstring
        """
        vvar = collatz_eval(100, 200)
        self.assertEqual(vvar, 125)

    def test_eval_3(self):
        """
        docstring
        """
        vvar = collatz_eval(201, 210)
        self.assertEqual(vvar, 89)

    def test_eval_4(self):
        """
        docstring
        """
        vvar = collatz_eval(900, 1000)
        self.assertEqual(vvar, 174)

    # -----
    # print
    # -----

    def test_print(self):
        """
        docstring
        """
        wvar = StringIO()
        collatz_print(wvar, 1, 10, 20)
        self.assertEqual(wvar.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        docstring
        """
        rvar = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        wvar = StringIO()
        collatz_solve(rvar, wvar)
        self.assertEqual(wvar.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
