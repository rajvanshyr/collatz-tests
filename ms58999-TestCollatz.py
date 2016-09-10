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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        test_string = "1 10\n"
        i, j = collatz_read(test_string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_1(self):
        test_string = "59 1000\n"
        i, j = collatz_read(test_string)
        self.assertEqual(i, 59)
        self.assertEqual(j, 1000)

    def test_read_2(self):
        test_string = "123456 987654\n"
        i, j = collatz_read(test_string)
        self.assertEqual(i, 123456)
        self.assertEqual(j, 987654)

    def test_read_3(self):
        test_string = "42 24\n"
        i, j = collatz_read(test_string)
        self.assertEqual(i, 42)
        self.assertEqual(j, 24)

    # ------------
    #cycle_length
    #------------
    def test_cycle_length_1(self):
        cycle = collatz_cycle_length(5)
        self.assertEqual(6, cycle)

    def test_cycle_length_2(self):
        cycle = collatz_cycle_length(1234)
        self.assertEqual(133, cycle)

    def test_cycle_length_3(self):
        cycle = collatz_cycle_length(3001)
        self.assertEqual(41, cycle)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        test_values = collatz_eval(1, 10)
        self.assertEqual(test_values, 20)

    def test_eval_2(self):
        test_values = collatz_eval(100, 200)
        self.assertEqual(test_values, 125)

    def test_eval_3(self):
        test_values = collatz_eval(201, 210)
        self.assertEqual(test_values, 89)

    def test_eval_4(self):
        test_values = collatz_eval(900, 1000)
        self.assertEqual(test_values, 174)

    def test_eval_5(self):
        test_values = collatz_eval(1, 7)
        self.assertEqual(test_values, 17)

    def test_eval_6(self):
        test_values = collatz_eval(1000, 1013)
        self.assertEqual(test_values, 143)

    def test_eval_7(self):
        test_values = collatz_eval(3, 12)
        self.assertEqual(test_values, 20)

    def test_eval_8(self):
        test_values = collatz_eval(1, 1)
        self.assertEqual(test_values, 1)

    def test_eval_9(self):
        test_values = collatz_eval(1234, 9876)
        self.assertEqual(test_values, 262)

    def test_eval_10(self):
        test_values = collatz_eval(2000, 3000)
        self.assertEqual(test_values, 217)

    # -----
    # print
    # -----

    def test_print(self):
        test_output = StringIO()
        collatz_print(test_output, 1, 10, 20)
        self.assertEqual(test_output.getvalue(), "1 10 20\n")

    def test_print_1(self):
        test_output = StringIO()
        collatz_print(test_output, 5, 121, 32)
        self.assertEqual(test_output.getvalue(), "5 121 32\n")


    def test_print_2(self):
        test_output = StringIO()
        collatz_print(test_output, 1000, 1013, 142)
        self.assertEqual(test_output.getvalue(), "1000 1013 142\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        test_string = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        test_output = StringIO()
        collatz_solve(test_string, test_output)
        self.assertEqual(test_output.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1(self):
        test_string = StringIO("1 1\n1000 1013\n1 13\n1000000 1000000\n")
        test_output = StringIO()
        collatz_solve(test_string, test_output)
        self.assertEqual(test_output.getvalue(), "1 1 1\n1000 1013 143\n1 13 20\n1000000 1000000 153\n")

    def test_solve_2(self):
        test_string = StringIO("3 12\n1 7\n1 13\n41 45\n")
        test_output = StringIO()
        collatz_solve(test_string, test_output)
        self.assertEqual(test_output.getvalue(), "3 12 20\n1 7 17\n1 13 20\n41 45 110\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
