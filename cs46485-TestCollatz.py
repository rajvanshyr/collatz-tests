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

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print
from Collatz import collatz_solve, odd_n, dec_range, cycle_length

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # odd_n
    # ----

    def test_odd_n_1(self):
        """
        Runs odd_n function with the value 7 and should evaluated to 11.
        """
        ans = odd_n(7)
        self.assertEqual(ans, 11)

    def test_odd_n_2(self):
        """
        Runs odd_n function with the value 25 and should evaluated to 38.
        """
        ans = odd_n(25)
        self.assertEqual(ans, 38)

    def test_odd_n_3(self):
        """
        Runs odd_n function with the value 105 and should evaluated to 39.
        """
        ans = odd_n(105)
        self.assertEqual(ans, 158)

    # ----
    # dec_range
    # ----
    def test_dec_range_1(self):
        """
        Runs dec_range for values 1 and 10, should return 6.
        """
        beg = dec_range(1, 10)
        self.assertEqual(beg, 6)

    def test_dec_range_2(self):
        """
        Runs dec_range for values 30 and 35, should return 30.
        """
        beg = dec_range(30, 35)
        self.assertEqual(beg, 30)

    def test_dec_range_3(self):
        """
        Runs dec_range for values 100 and 200, should return 30.
        """
        beg = dec_range(100, 200)
        self.assertEqual(beg, 101)

    # ----
    # cycle_length
    # ----

    def cycle_length_1(self):
        """
        Runs cycle_length with value of 1
        Should run into the base case
        """
        cycle_len = cycle_length(1)
        self.assertEqual(cycle_len, 1)

    def cycle_length_2(self):
        """
        Runs cycle_length with value of 53
        Should return value of 12
        """
        cycle_len = cycle_length(53)
        self.assertEqual(cycle_len, 12)

    def cycle_length_3(self):
        """
        Runs cycle_length with value of 99999
        Should return value of 227
        """
        cycle_len = cycle_length(99999)
        self.assertEqual(cycle_len, 227)

    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Tests that values are being read properly
        """
        string = "1 10\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """
        Tests that values are being read properly
        """
        string = "10000 723\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 10000)
        self.assertEqual(end, 723)

    def test_read_3(self):
        """
        Tests that values are being read properly
        """
        string = "100 7233\n"
        beg, end = collatz_read(string)
        self.assertEqual(beg, 100)
        self.assertEqual(end, 7233)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Runs collatz_eval with values 20 and 100
        Should return max_cycle_length of 119
        """
        ans = collatz_eval(20, 100)
        self.assertEqual(ans, 119)

    def test_eval_2(self):
        """
        Runs collatz_eval with values 1 and 999999
        Should return max_cycle_length of 119
        """
        ans = collatz_eval(1, 999999)
        self.assertEqual(ans, 525)

    def test_eval_3(self):
        """
        Runs collatz_eval with values 40000 and 20
        Should return max_cycle_length of 324
        """
        ans = collatz_eval(40000, 20)
        self.assertEqual(ans, 324)

    def test_eval_4(self):
        """
        Runs collatz_eval with values 1 and 2
        Should return max_cycle_length of 2
        """
        ans = collatz_eval(1, 2)
        self.assertEqual(ans, 2)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        Tests the writer
        """
        writer = StringIO()
        collatz_print(writer, 20, 100, 119)
        self.assertEqual(writer.getvalue(), "20 100 119\n")

    def test_print_2(self):
        """
        Tests the writer
        """
        writer = StringIO()
        collatz_print(writer, 40000, 20, 324)
        self.assertEqual(writer.getvalue(), "40000 20 324\n")

    def test_print_3(self):
        """
        Tests the writer
        """
        writer = StringIO()
        collatz_print(writer, 1, 1, 1)
        self.assertEqual(writer.getvalue(), "1 1 1\n")
        writer = StringIO()
        collatz_print(writer, 40000, 20, 324)
        self.assertEqual(writer.getvalue(), "40000 20 324\n")

    # -----
    # solve
    # -----

    def test_solve_empty(self):
        """
        Tests the solver, writer, and reader
        Makes sure the right value is received and printed
        Checks to see if empty strings are handled correctly
        """
        reader = StringIO("719 6121\n\n1 23945\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "719 6121 238\n1 23945 282\n")

    def test_solve_1(self):
        """
        Tests the solver, writer, and reader
        Makes sure the right value is received and printed
        """

    def test_solve(self):
        """
        Tests the solver, writer, and reader
        Makes sure the right value is received and printed
        """
        reader = StringIO("20 100\n1 999999\n40000 20\n1 2\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "20 100 119\n1 999999 525\n40000 20 324\n1 2 2\n")

    def test_solve_2(self):
        """
        Tests the solver, writer, and reader
        Makes sure the right value is received and printed
        """
        reader = StringIO("1 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 1 1\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()