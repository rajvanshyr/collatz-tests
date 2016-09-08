#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt
"""Unit white box tests for collatz."""

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
    """Unit tests for the Collatz problem."""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Assert that read works properly."""
        input_string = "1 10\n"
        first, second = collatz_read(input_string)
        self.assertEqual(first, 1)
        self.assertEqual(second, 10)

    def test_read_2(self):
        """Assert proper read actions again."""
        input_string = "200 1000\n"
        first, second = collatz_read(input_string)
        self.assertEqual(first, 200)
        self.assertEqual(second, 1000)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        """Assert that  evaluating the longest cycle length between 1 and 10 is 20."""
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        """Assert that  evaluating the longest cycle length between 100 and 200 is 125."""
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        """Assert that  evaluating the longest cycle length between 201 and 210 is 89."""
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        """Assert that  evaluating the longest cycle length between 900 and 1000 is 174."""
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    # -----
    # print
    # -----
    def test_print(self):
        """Assert that print is working properly."""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """Assert print is working properly with more values."""
        writer = StringIO()
        collatz_print(writer, 20, 800, 23)
        self.assertEqual(writer.getvalue(), "20 800 23\n")

    # -----
    # solve
    # -----
    def test_solve(self):
        """Assert that reading in a long string works the same way as small inputs."""
        read_string = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(read_string, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """Assert extra test for long string processing."""
        read_string = StringIO("10823 43615\n30594 59978\n2633 26475\n")
        writer = StringIO()
        collatz_solve(read_string, writer)
        self.assertEqual(writer.getvalue(), "10823 43615 324\n30594 59978 340\n2633 26475 282\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
