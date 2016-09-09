#!/usr/bin/env python3
"""
Unittest suite for Collatz.py
"""
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_solve_single

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # pylint: disable=C0111

    # ----
    # read
    # ----

    def test_read(self):
        """
        Unittest that we are receiving a list with the two integers we sent in STDin
        """
        test_input = "1 10\n"
        start, end = collatz_read(test_input)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_1(self):
        test_input = "10 1\n"
        start, end = collatz_read(test_input)
        self.assertEqual(start, 10)
        self.assertEqual(end, 1)

    # ----
    # find single max cycle length
    # ---

    def test_solve_single_1(self):
        cycle_length = collatz_solve_single(5)
        self.assertEqual(cycle_length, 6)

    def test_solve_single_2(self):
        cycle_length = collatz_solve_single(1)
        self.assertEqual(cycle_length, 1)

    def test_solve_single_3(self):
        cycle_length = collatz_solve_single(2)
        self.assertEqual(cycle_length, 2)

    def test_solve_single_4(self):
        cycle_length = collatz_solve_single(10)
        self.assertEqual(cycle_length, 7)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        value = collatz_eval(1, 2)
        self.assertEqual(value, 2)

    def test_eval_6(self):
        value = collatz_eval(1, 5)
        self.assertEqual(value, 8)

    def test_eval_7(self):
        value = collatz_eval(1, 6000)
        self.assertEqual(value, 238)

    def test_eval_8(self):
        """
        Test results are as expected even when order of range input is flipped
        """
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    # -----
    # print
    # -----

    def test_print(self):
        """
        Unittest that collatz_print prints three expected integers
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_correct_order(self):
        """
        Unittest that collatz_print prints the number in the inputted order
        """
        writer = StringIO()
        collatz_print(writer, 10, 1, 20)
        self.assertEqual(writer.getvalue(), "10 1 20\n")

    def test_print_(self):
        """
        Unittest that collatz_print doesn't drop a number if the start and end
        range are the same
        """
        writer = StringIO()
        collatz_print(writer, 5, 5, 6)
        self.assertEqual(writer.getvalue(), "5 5 6\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        Test that collatz_solve works prints twelve expected ouputs given 8 inputs
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_empty(self):
        """
        Test that collatz_solve works when given input with trailing whitespace
        """
        reader = StringIO("   \n   1 10\n\n\n1 10\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n1 10 20\n")

# ----
# main
# ----

if __name__ == "__main__":  # pragma: no cover
    main()
