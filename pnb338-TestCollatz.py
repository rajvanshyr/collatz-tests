#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

""" Collatz Test Harness """

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_meta, collatz_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    class for unit testing Collatz
    """

    # ----
    # meta
    # ----

    def test_meta_1(self):
        """
        test meta cache functionality
        """
        begin = 1500
        end = 4500
        tiling = 200
        max_cycle = collatz_meta(begin, end, tiling)
        self.assertEqual(max_cycle, 238)

    def test_meta_2(self):
        """
        test meta cache functionality
        """
        begin = 1000
        end = 2000
        tiling = 200
        max_cycle = collatz_meta(begin, end, tiling)
        self.assertEqual(max_cycle, 182)

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        """
        test cycle length functionality
        """
        num = 5
        cycle_length = collatz_cycle_length(num)
        self.assertEqual(cycle_length, 6)

    def test_cycle_length_2(self):
        """
        test cycle length functionality
        """
        num = 10
        cycle_length = collatz_cycle_length(num)
        self.assertEqual(cycle_length, 7)

    def test_cycle_length_3(self):
        """
        test cycle length functionality
        """
        num = 999999
        cycle_length = collatz_cycle_length(num)
        self.assertEqual(cycle_length, 259)

    # ----
    # read
    # ----

    def test_read(self):
        """
        test of reading functionality
        """
        line = "1 10\n"
        begin, end = collatz_read(line)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        test of evaluation functionality
        """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """
        test of evaluation functionality
        """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """
        test of evaluation functionality
        """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """
        test of evaluation functionality
        """
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        """
        test of evaluation functionality
        """
        val = collatz_eval(1, 5000)
        self.assertEqual(val, 238)

    # -----
    # print
    # -----

    def test_print(self):
        """
        test of printing functionality
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO("10 1\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "10 1 20\n")

    def test_solve_3(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO(" \n1 10\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_solve_4(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO("\t\n1 10\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_solve_5(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO("10 10\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "10 10 7\n")

    def test_solve_6(self):
        """
        test of overall Collatz functionality
        """
        reader = StringIO("1500 4500\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1500 4500 238\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
