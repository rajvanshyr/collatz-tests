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
This file is a test suite for collatz
"""

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve
from Collatz import collatz_run, eval_first_range, eval_second_range, eval_mid_range
from Collatz import order_first_second

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # pylint: disable=R0904
    """
    Test Suite
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        test read
        """
        string = "1 10\n"
        first_number, second_number = collatz_read(string)
        self.assertEqual(first_number, 1)
        self.assertEqual(second_number, 10)

    def test_read_2(self):
        """
        test read
        """
        string = "111 11\n"
        first_number, second_number = collatz_read(string)
        self.assertEqual(first_number, 111)
        self.assertEqual(second_number, 11)

    def test_read_3(self):
        """
        test read
        """
        string = "0 00000\n"
        first_number, second_number = collatz_read(string)
        self.assertEqual(first_number, 0)
        self.assertEqual(second_number, 00000)

    # ----
    # first range
    # ----

    def test_eval_first_1(self):
        """
        test first 1
        """
        value = eval_first_range(22)
        self.assertEqual(value[0], 0)

    def test_eval_first_2(self):
        """
        test first 2
        """
        value = eval_first_range(522)
        self.assertEqual(value[1], 22)

    def test_eval_first_3(self):
        """
        test first 3
        """
        value = eval_first_range(22)
        self.assertEqual(value[2], 499)

    # ----
    # second range
    # ----

    def test_eval_second_1(self):
        """
        test second 1
        """
        value = eval_second_range(22)
        self.assertEqual(value[0], 0)

    def test_eval_second_2(self):
        """
        test second 2
        """
        value = eval_second_range(522)
        self.assertEqual(value[1], 22)

    def test_eval_second_3(self):
        """
        test second 3
        """
        value = eval_second_range(500)
        self.assertEqual(value[2], 500)

    # ----
    # mid range
    # ----

    def test_mid_1(self):
        """
        test mid 1
        """
        max_values = []
        eval_mid_range(0, 3, max_values)
        self.assertEqual(len(max_values), 2)

    def test_mid_2(self):
        """
        test mid 2
        """
        max_values = []
        eval_mid_range(1, 3, max_values)
        self.assertEqual(max_values[0], 182)

    def test_mid_3(self):
        """
        test mid 3
        """
        max_values = []
        eval_mid_range(0, 5, max_values)
        self.assertEqual(max(max_values), 209)

    # ----
    # order
    # ----

    def test_order_1(self):
        """
        test order 1
        """
        value = order_first_second(2, 1)
        self.assertEqual(value[0], 1)

    def test_order_2(self):
        """
        test order 2
        """
        value = order_first_second(2, 1)
        self.assertEqual(value[1], 2)

    def test_order_3(self):
        """
        test order 3
        """
        value = order_first_second(2, 3)
        self.assertEqual(value[1], 3)

    # ----
    # run
    # ----

    def test_run_1(self):
        """
        test 1
        """
        value = collatz_run(1, 10)
        self.assertEqual(value, 20)

    def test_run_2(self):
        """
        test 2
        """
        value = collatz_run(100, 200)
        self.assertEqual(value, 125)

    def test_run_3(self):
        """
        test 3
        """
        value = collatz_run(201, 210)
        self.assertEqual(value, 89)

    def test_run_4(self):
        """
        test 4
        """
        value = collatz_run(900, 1000)
        self.assertEqual(value, 174)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        test 1
        """
        value = collatz_eval(0, 1)
        self.assertEqual(value, 0)

    def test_eval_2(self):
        """
        test 2
        """
        value = collatz_eval(1, 0)
        self.assertEqual(value, 0)

    def test_eval_3(self):
        """
        test 3
        """
        value = collatz_eval(0, 0)
        self.assertEqual(value, 0)

    def test_eval_4(self):
        """
        test 4
        """
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        test
        """
        word = StringIO()
        collatz_print(word, 1, 10, 20)
        self.assertEqual(word.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        test
        """
        word = StringIO()
        collatz_print(word, 100, 200, 125)
        self.assertEqual(word.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        test
        """
        word = StringIO()
        collatz_print(word, 201, 210, 89)
        self.assertEqual(word.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        test solve
        """
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        word = StringIO()
        collatz_solve(read, word)
        self.assertEqual(word.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
