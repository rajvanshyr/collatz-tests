#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt
"""
Module for testing Collatz.py
"""
# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_solve_single

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Test class for Collaatz.py
    Inherits the class TestCase so that it can use the assertEquals methods
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
        Unit test testing the functionality of collatz_read
        :return:
        """
        line = "1 10\n"
        start_index, end_index = collatz_read(line)
        self.assertEqual(start_index, 1)
        self.assertEqual(end_index, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Unit test for collatz_eval with range 1-10
        :return:
        """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    def test_eval_2(self):
        """
        Unit test for collatz_eval with range 100-200
        :return:
        """
        max_cycle = collatz_eval(100, 200)
        self.assertEqual(max_cycle, 125)

    def test_eval_3(self):
        """
        Unit test for collatz_eval with range 201-210
        :return:
        """
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_4(self):
        """
        Unit test for collatz_eval with range 900-1000
        :return:
        """
        max_cycle = collatz_eval(900, 1000)
        self.assertEqual(max_cycle, 174)

    def test_eval_5(self):
        """
        Unit test test large range that spans across several thousands of integers
        :return:
        """
        max_cycle = collatz_eval(572556, 815799)
        self.assertEqual(max_cycle, 509)

    def test_eval_6(self):
        """
        Unit test test large range that spans across several thousands of integers
        :return:
        """
        max_cycle = collatz_eval(815799, 572556)
        self.assertEqual(max_cycle, 509)

    def test_single(self):
        """
        Test the single solve method
        :return:
        """
        cache = {}
        max_cycle = collatz_solve_single(10, cache)
        self.assertEqual(max_cycle, 7)

    def test_single_2(self):
        """
         Test the single solve method
         :return:
         """
        cache = {}
        max_cycle = collatz_solve_single(1, cache)
        self.assertEqual(max_cycle, 1)

    def test_single_3(self):
        """
         Test the single solve method
         :return:
         """
        cache = {}
        max_cycle = collatz_solve_single(100, cache)
        self.assertEqual(max_cycle, 26)
    # -----
    # print
    # -----

    def test_print(self):
        """
        Unit test testing the printing functionality
        :return:
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Unit test testing the printing functionality
        :return:
        """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        Unit test testing the printing functionality
        :return:
        """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        Integration Test reading multiple lines, passing them to collatz_eval,
        and getting a max cycle length for each range
        :return:
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
                Integration Test reading multiple lines, passing them to collatz_eval,
                and getting a max cycle length for each range
                :return:
                """
        reader = StringIO("   \n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "")

# ----
# main
# ----

if __name__ == "__main__":
    main()
