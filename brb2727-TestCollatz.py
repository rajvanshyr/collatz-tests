#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

"""
Test harness for collatz conjecture program
"""

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase, expectedFailure

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Unit Test Class
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Tests the collatz_read function
        """
        string = "1 10\n"
        range_start, range_end = collatz_read(string)
        self.assertEqual(range_start, 1)
        self.assertEqual(range_end, 10)

    def test_read_2(self):
        """
        Tests the collatz_read function with really large numbers.
        Apparently this works, must use 64-bit or higher representation?
        """
        string = "1000000000000 1000000000000\n"
        range_start, range_end = collatz_read(string)
        self.assertEqual(range_start, 1000000000000)
        self.assertEqual(range_end, 1000000000000)

    @staticmethod
    @expectedFailure
    def test_read_3():
        """
        Tests the collatz_read function with faulty input (non integers)
        Expected to fail.
        """
        string = "a b\n"
        collatz_read(string)

    # ----
    # cycle_length
    # ----

    def test_cycle_1(self):
        """
        Tests the cycle_length function
        """
        cycle = cycle_length(1)
        self.assertEqual(cycle, 1)

    def test_cycle_2(self):
        """
        Tests the cycle_length function
        """
        cycle = cycle_length(5)
        self.assertEqual(cycle, 6)

    def test_cycle_3(self):
        """
        Tests the cycle_length function
        """
        cycle = cycle_length(10)
        self.assertEqual(cycle, 7)

    def test_cycle_4(self):
        """
        Tests the cycle_length function
        """
        cycle = cycle_length(1000001)
        self.assertEqual(cycle, 114)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Tests the collatz_eval function
        """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    def test_eval_2(self):
        """
        Tests the collatz_eval function
        """
        max_cycle = collatz_eval(100, 200)
        self.assertEqual(max_cycle, 125)

    def test_eval_3(self):
        """
        Tests the collatz_eval function
        """
        max_cycle = collatz_eval(201, 210)
        self.assertEqual(max_cycle, 89)

    def test_eval_4(self):
        """
        Tests the collatz_eval function
        """
        max_cycle = collatz_eval(900, 1000)
        self.assertEqual(max_cycle, 174)

    def test_eval_5(self):
        """
        Tests the collatz_eval function and
        repeats so it makes use of the cache
        """
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)
        max_cycle = collatz_eval(1, 10)
        self.assertEqual(max_cycle, 20)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Tests the collatz_print function
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Tests the collatz_print function with really large integers
        """
        writer = StringIO()
        collatz_print(writer, "1000000000000",
                      "1000000000000", "1000000000000")
        self.assertEqual(writer.getvalue(),
                         "1000000000000 1000000000000 1000000000000\n")

    def test_print_3(self):
        """
        Tests the collatz_print function with non integers
        """
        writer = StringIO()
        collatz_print(writer, "a", "b", "c")
        self.assertEqual(writer.getvalue(), "a b c\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        Tests the collatz_solve function
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_backwards(self):
        """
        Tests the collatz_solve function where ranges are specified backwards
        """
        reader = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_mixed_order(self):
        """
        Tests the collatz_solve function where ranges are specified in a mixed
        way of being backwards and forwards
        """
        reader = StringIO("10 1\n100 200\n201 210\n1000 900\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "10 1 20\n100 200 125\n201 210 89\n1000 900 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
