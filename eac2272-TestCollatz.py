#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

"""
This document tests the Collatz python file
"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, max_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    Tests various aspects of the Collatz Methods
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """Test read normal input"""
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """Test read reverse input"""
        string = "10 1\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 10)
        self.assertEqual(end, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test 1"""
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    def test_eval_2(self):
        """Test 2"""
        value = collatz_eval(3, 3)
        self.assertEqual(value, 8)

    def test_eval_3(self):
        """Test 3"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """Test 4"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    # ----
    # cycle_length
    # ----

    def test_c_length_1(self):
        """Test 1"""
        value = max_cycle_length(1, 1)
        self.assertEqual(value, 1)

    def test_c_length_2(self):
        """Test 2"""
        value = max_cycle_length(3, 3)
        self.assertEqual(value, 8)

    def test_c_length_3(self):
        """Test 3"""
        value = max_cycle_length(999999, 999999)
        self.assertEqual(value, 259)

    def test_c_length_4(self):
        """Test 4, expect it to be off by 1"""
        value = max_cycle_length(258989, 258989)
        self.assertNotEqual(value, 119)

    # -----
    # print
    # -----

    def test_print(self):
        """Test print"""
        write = StringIO()
        collatz_print(write, 1, 100, 119)
        self.assertEqual(write.getvalue(), "1 100 119\n")

    # -----
    # solve
    # -----

    def test_solve_normal(self):
        """Test solve"""
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_inverse(self):
        """Some inputs are backwards"""
        read = StringIO("10 1\n200 100\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "10 1 20\n200 100 125\n201 210 89\n900 1000 174\n")

    def test_solve_crazy(self):
        """normal, inverse and same value for range"""
        read = StringIO("10 1\n200 100\n201 210\n3 3\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "10 1 20\n200 100 125\n201 210 89\n3 3 8\n")

    def test_solve_repeats(self):
        """ensure no logic error with repeat numbers"""
        read = StringIO("1 1\n1 1\n3 3\n3 3\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "1 1 1\n1 1 1\n3 3 8\n3 3 8\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
