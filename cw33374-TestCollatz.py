#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

""" Family of tests for Collatz.py """

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, CACHE

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """ Tests all functions in Collatz.py """
    # ----
    # read
    # ----

    def test_read(self):
        """ Tests collatz_read() """
        src = "1 10\n"
        i, j = collatz_read(src)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ Tests collatz_eval(1, 10)"""
        mcl = collatz_eval(1, 10)
        self.assertEqual(mcl, 20)

    def test_eval_2(self):
        """ Tests collatz_eval(100, 200)"""
        mcl = collatz_eval(100, 200)
        self.assertEqual(mcl, 125)

    def test_eval_3(self):
        """ Tests collatz_eval(201, 210)"""
        mcl = collatz_eval(201, 210)
        self.assertEqual(mcl, 89)

    def test_eval_4(self):
        """ Tests collatz_eval(900, 1000)"""
        mcl = collatz_eval(900, 1000)
        self.assertEqual(mcl, 174)

    def test_eval_reverse(self):
        """ Test collatz_eval(10, 1) """
        mcl = collatz_eval(10, 1)
        self.assertEqual(mcl, 20)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_base(self):
        """ Tests cycle_length(1) """
        length = cycle_length(1)
        self.assertEqual(length, 1)

    def test_cycle_even(self):
        """ Tests cycle_length(2) """
        length = cycle_length(2)
        self.assertEqual(length, 2)

    def test_cycle_odd(self):
        """ Tests cycle_length(5) """
        length = cycle_length(5)
        self.assertEqual(length, 6)

    def test_cycle_invalid(self):
        """ Tests cycle_length on invalid domain """
        with self.assertRaises(AssertionError):
            cycle_length(-1)

    def test_cycle_large(self):
        """ Tests cycle_length on large values """
        length = cycle_length(999699)
        self.assertEqual(length, 184)

    def test_cycle_cache(self):
        """ Test that the cache has the right things after a computation """
        CACHE.clear()
        cycle_length(5)
        self.assertEqual(CACHE[5], 6)
        self.assertEqual(CACHE[8], 4)
        self.assertEqual(CACHE[4], 3)
        self.assertEqual(CACHE[2], 2)
        self.assertEqual(CACHE[1], 1)

    # -----
    # print
    # -----

    def test_print(self):
        """ Tests collatz_print() """
        out = StringIO()
        collatz_print(out, 1, 10, 20)
        self.assertEqual(out.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """ Tests collatz_solve() """
        src = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        out = StringIO()
        collatz_solve(src, out)
        self.assertEqual(
            out.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_empty(self):
        """ Tests collatz_solve on an empty dataset """
        src = StringIO("")
        out = StringIO()
        collatz_solve(src, out)
        self.assertEqual(out.getvalue(), "")

    def test_solve_blank_line(self):
        """ Tests collatz_solve on input with blank lines """
        src = StringIO("1 10\n100 200\n201 210\n\t  \n900 1000\n")
        out = StringIO()
        collatz_solve(src, out)
        self.assertEqual(
            out.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
