#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""Tests harnesses for Collatz"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, CACHE
"""CACHE is specfic to my implementation"""


# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """Test harness"""

    # ----
    # read
    # ----

    def test_read_1(self):
        """Basic read functionality"""
        line = "1 10\n"
        begin, end = collatz_read(line)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """Read input in exactly, even if reversed"""
        line = "999 1\n"
        begin, end = collatz_read(line)
        self.assertEqual(begin, 999)
        self.assertEqual(end, 1)

    def test_read_4(self):
        """Additional ints in a line are ignored"""
        line = "10 20 30 40 50\n"
        begin, end = collatz_read(line)
        self.assertEqual(begin, 10)
        self.assertEqual(end, 20)

    def test_read_5(self):
        """Short of input should break in read"""
        error = False
        try:
            collatz_read("1\n")
        except IndexError:
            error = True
        self.assertTrue(error)

    # ----
    # eval
    # ----


    def test_eval_1(self):
        """Correctness: 89"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_2(self):
        """Correctness: 174"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_3(self):
        """Reversed range performs normal"""
        value = collatz_eval(312, 42)
        self.assertEqual(value, 128)

    def test_eval_4(self):
        """Correctness: 259; and test for-loop exec"""
        value = collatz_eval(999999, 999999)
        self.assertEqual(value, 259)

    def test_eval_5(self):
        """Corectness for longest path"""
        value = collatz_eval(837799, 837799)
        self.assertEqual(value, 525)

    # -----
    # cache
    # -----

    def test_cache_1(self):
        """While evaluating 3, 5 should be cached correctly"""
        collatz_eval(3, 3)
        self.assertEqual(CACHE[5], 6)

    def test_cache_2(self):
        """While evaluating 3, 25 should not be cached"""
        collatz_eval(3, 3)
        self.assertFalse(25 in CACHE)

    def test_cache_3(self):
        """Testing cache for a larger range"""
        collatz_eval(1, 312)
        self.assertEqual(CACHE[156], 37)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Basic print functionality"""
        output = StringIO()
        collatz_print(output, 1, 10, 20)
        self.assertEqual(output.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """Reversed range executes, but prints same as input"""
        output = StringIO()
        collatz_print(output, 20, 10, 21)
        self.assertEqual(output.getvalue(), "20 10 21\n")

    def test_print_3(self):
        """Test bogus numbers"""
        output = StringIO()
        collatz_print(output, -10, 0, 999999999999999999999)
        self.assertEqual(output.getvalue(), "-10 0 999999999999999999999\n")

    # -----
    # solve
    # -----
    def test_solve_1(self):
        """Basic read and print functionality"""
        inln = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        output = StringIO()
        collatz_solve(inln, output)
        self.assertEqual(
            output.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """Skip empty lines"""
        inln = StringIO("\n\n1 10\n\n100 200\n")
        output = StringIO()
        collatz_solve(inln, output)
        self.assertEqual(
            output.getvalue(), "1 10 20\n100 200 125\n")

    def test_solve_3(self):
        """Reverse range, but print input and eval"""
        inln = StringIO("200 100\n")
        output = StringIO()
        collatz_solve(inln, output)
        self.assertEqual(
            output.getvalue(), "200 100 125\n")

    def test_solve_4(self):
        """Additional input should be ignored"""
        inln = StringIO("10 20 30 40 50 60 70\n")
        output = StringIO()
        collatz_solve(inln, output)
        self.assertEqual(
            output.getvalue(), "10 20 21\n")

    def test_solve_5(self):
        """Combination of all solve tests"""
        inln = StringIO("\n\n20 1 15 100 60 78\n")
        output = StringIO()
        collatz_solve(inln, output)
        self.assertEqual(
            output.getvalue(), "20 1 21\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
