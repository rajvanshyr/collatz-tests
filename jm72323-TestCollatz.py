#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------
""" A test harness for Collatz. """

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import (collatz_read,
                     collatz_eval,
                     collatz_print,
                     collatz_solve,
                     calc_collatz)

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """ A class for testing Collatz. """

    # ----
    # read
    # ----

    def test_read(self):
        """ Read test 1 """
        string = "1 10\n"
        first_num, second_num = collatz_read(string)
        self.assertEqual(first_num, 1)
        self.assertEqual(second_num, 10)

    def test_read_2(self):
        """ Read test 2 """
        string = "100 200\n"
        first_num, second_num = collatz_read(string)
        self.assertEqual(first_num, 100)
        self.assertEqual(second_num, 200)

    def test_read_3(self):
        """ Read test 3 """
        string = "201 210\n"
        first_num, second_num = collatz_read(string)
        self.assertEqual(first_num, 201)
        self.assertEqual(second_num, 210)

    # -------------
    # calculate collatz
    # -------------

    def test_calc_collatz(self):
        """
        Test calculating the max cycle length of one number
        """
        max_cycle = calc_collatz(1, {})
        self.assertEqual(max_cycle, 1)

    def test_calc_collatz_2(self):
        """ Collatz calculation test 2 """
        max_cycle = calc_collatz(10, {})
        self.assertEqual(max_cycle, 7)

    def test_calc_collatz_3(self):
        """ Collatz calculation test 3 """
        max_cycle = calc_collatz(160, {})
        self.assertEqual(max_cycle, 11)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ Test calculating the correct max cycle """
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """ Eval test 2 """
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """ Eval test 3 """
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """ Eval test 4 """
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """ Eval test 5 inverse first and second """
        value = collatz_eval(1000, 900)
        self.assertEqual(value, 174)

    def test_eval_6(self):
        """ Eval test6 """
        value = collatz_eval(999900, 1000000)
        self.assertEqual(value, 259)

    # -----
    # print
    # -----

    def test_print(self):
        """ Tests printing the values to the output. """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """ Test printing 2 """
        writer = StringIO()
        collatz_print(writer, 100, 200, 125)
        self.assertEqual(writer.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """ Test printing 3 """
        writer = StringIO()
        collatz_print(writer, 201, 210, 89)
        self.assertEqual(writer.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """ Tests solving for multiple input values. """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """ Tests solve 2 """
        reader = StringIO("1 200\n1 1000\n1 10000\n200 200000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "1 200 125\n1 1000 179\n1 10000 262\n200 200000 383\n")

    def test_solve_3(self):
        """ Tests solve 3, whitespace only """
        reader = StringIO("        ")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__":
    main()
