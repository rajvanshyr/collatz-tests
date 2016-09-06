#!/usr/bin/env python3
"""This is a python file"""
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """Tests"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Does read work?"""
        stream = "1 10\n"
        i, j = collatz_read(stream)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """Does read work?"""
        stream = "3 5\n"
        i, j = collatz_read(stream)
        self.assertEqual(i, 3)
        self.assertEqual(j, 5)

    def test_read_3(self):
        """Does read work?"""
        stream = "100 500\n"
        i, j = collatz_read(stream)
        self.assertEqual(i, 100)
        self.assertEqual(j, 500)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        """Does eval work?"""
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """Does eval work?"""
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """Does eval work?"""
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """Does eval work?"""
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    # -----
    # print
    # -----

    def test_print1(self):
        """Does print work?"""
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    def test_print2(self):
        """Does print work?"""
        write = StringIO()
        collatz_print(write, 100, 200, 125)
        self.assertEqual(write.getvalue(), "100 200 125\n")

    def test_print3(self):
        """Does print work?"""
        write = StringIO()
        collatz_print(write, 201, 210, 89)
        self.assertEqual(write.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Does solve work?"""
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """Does solve work?"""
        read = StringIO("492 2460\n951 2853\n324 1296\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "492 2460 183\n951 2853 209\n324 1296 182\n")

    def test_solve_3(self):
        """Does solve work?"""
        read = StringIO("2772 693\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "2772 693 209\n")

    # ------------
    # cycle length
    # ------------

    def test_cycle_1(self):
        """Does cycle length work?"""
        num = 5
        cylen = cycle_length(1, num)
        self.assertEqual(cylen, 6)

    def test_cycle_2(self):
        """Does cycle length work?"""
        num = 10
        cylen = cycle_length(1, num)
        self.assertEqual(cylen, 7)

    def test_cycle_3(self):
        """Does cycle length work?"""
        num = 25
        cylen = cycle_length(1, num)
        self.assertEqual(cylen, 24)

# ----
# main
# ----

if __name__ == "__main__":
    main()
