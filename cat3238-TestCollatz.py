#!/usr/bin/env python3
"""Unit Tests for Collatz.py"""

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_meta

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """Unit Tests for Collatz.py"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Test collatz_read for a range"""
        string = "1 10\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 1)
        self.assertEqual(input_j, 10)

    def test_read_2(self):
        """Test collatz_read for a range (i == j)"""
        string = "100 100\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 100)
        self.assertEqual(input_j, 100)

    def test_read_3(self):
        """Test collatz_read for a range (i > j)"""
        string = "99999 1\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 99999)
        self.assertEqual(input_j, 1)

    def test_read_4(self):
        """Test collatz_read for a range (i < j)"""
        string = "0 1000000\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 0)
        self.assertEqual(input_j, 1000000)

    def test_read_5(self):
        """Test collatz_read for a range with a single number"""
        string = "1\n"
        err = False
        try:
            collatz_read(string)
        except IndexError:
            err = True
        self.assertTrue(err)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test collatz_eval for (0, 0)"""
        val = collatz_eval(0, 0)
        self.assertEqual(val, 1)

    def test_eval_2(self):
        """Test collatz_eval for (210, 201)"""
        val = collatz_eval(210, 201)
        self.assertEqual(val, 89)

    def test_eval_3(self):
        """Test collatz_eval for (486026, 719622)"""
        val = collatz_eval(486026, 719622)
        self.assertEqual(val, 509)

    def test_eval_4(self):
        """Test collatz_eval for (1000000, 0)"""
        val = collatz_eval(1000000, 0)
        self.assertEqual(val, 525)

    # ----
    # meta
    # ----

    def test_meta_1(self):
        """Test collatz_meta for (1, 10)"""
        val = collatz_meta(1, 10)
        self.assertEqual(val, (1, [1, 10], [1, 1], [1, 1]))

    def test_meta_2(self):
        """Test collatz_meta for (222, 99999)"""
        val = collatz_meta(222, 99999)
        self.assertEqual(val, (351, [222, 99999], [222, 250], [99876, 99999]))

    def test_meta_3(self):
        """Test collatz_meta for (217129, 40021)"""
        val = collatz_meta(217129, 40021)
        self.assertEqual(
            val, (386, [40021, 217129], [40021, 40125], [217126, 217129]))

    def test_meta_4(self):
        """Test collatz_meta for (821650, 3431)"""
        val = collatz_meta(821650, 3431)
        self.assertEqual(
            val, (509, [3431, 821650], [3431, 3500], [821626, 821650]))

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test collatz_print for a range with correct result"""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """Test collatz_print for a range with incorrect result"""
        writer = StringIO()
        collatz_print(writer, 55555, 55555, 55555)
        self.assertEqual(writer.getvalue(), "55555 55555 55555\n")

    def test_print_3(self):
        """Test collatz_print for a range with correct result"""
        writer = StringIO()
        collatz_print(writer, 821650, 3431, 509)
        self.assertEqual(writer.getvalue(), "821650 3431 509\n")

    def test_print_4(self):
        """Test collatz_print for a range with correct result"""
        writer = StringIO()
        collatz_print(writer, 0, 1000000, 525)
        self.assertEqual(writer.getvalue(), "0 1000000 525\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test collatz_solve for multiple ranges"""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """Test collatz_solve for a single range"""
        reader = StringIO("1 1000000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 1000000 525\n")

    def test_solve_3(self):
        """Test collatz_solve for multple ranges with whitespaces and blank lines"""
        reader = StringIO("3431 821650\n \n222 99999\n\n486026 719622\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "3431 821650 509\n222 99999 351\n486026 719622 509\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
