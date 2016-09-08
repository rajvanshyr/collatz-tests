"""__TestCollatz__"""
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

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """__TestCollatz__"""
    # ----
    # read
    # ----

    def test_read(self):
        """__test_read"""
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """__test_read_2"""
        string = "4564 85454\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 4564)
        self.assertEqual(j, 85454)

    def test_read_3(self):
        """__test_read"""
        string = "36247 76548\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 36247)
        self.assertEqual(j, 76548)

    # ----
    # cycle_length
    # ----
    def test_cycle_length(self):
        """test_cycle_length"""
        length = cycle_length(56413, 0)
        self.assertEqual(length, 61)

    def test_cycle_length_2(self):
        """test_cycle_length_2"""
        length = cycle_length(1, 0)
        self.assertEqual(length, 1)

    def test_cycle_length_3(self):
        """test_cycle_length_3"""
        length = cycle_length(6666, 0)
        self.assertEqual(length, 32)
    # ----
    # eval
    # ----

    def test_eval_1(self):
        """__test_eval_1"""
        evaluation = collatz_eval(56413, 2184)
        self.assertEqual(evaluation, 340)

    def test_eval_2(self):
        """__test_eval_2"""
        evaluation = collatz_eval(6542, 78964)
        self.assertEqual(evaluation, 351)

    def test_eval_3(self):
        """__test_eval_3"""
        evaluation = collatz_eval(5523, 10005)
        self.assertEqual(evaluation, 262)

    def test_eval_4(self):
        """__test_eval_4"""
        evaluation = collatz_eval(33321, 5000)
        self.assertEqual(evaluation, 308)

    # -----
    # print
    # -----

    def test_print(self):
        """__test_print"""
        writer = StringIO()
        collatz_print(writer, 56413, 2184, 340)
        self.assertEqual(writer.getvalue(), "56413 2184 340\n")

    def test_print_2(self):
        """__test_print_2"""
        writer = StringIO()
        collatz_print(writer, 5523, 10005, 262)
        self.assertEqual(writer.getvalue(), "5523 10005 262\n")

    def test_print_3(self):
        """__test_print_3"""
        writer = StringIO()
        collatz_print(writer, 33321, 5000, 125)
        self.assertEqual(writer.getvalue(), "33321 5000 125\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """__test_solve"""
        reader = StringIO("5 66\n666 789\n999 10086\n5112 1994\n\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "5 66 113\n666 789 171\n999 10086 262\n5112 1994 238\n")

    def test_solve_2(self):
        """__test_solve_2"""
        reader = StringIO("100 100\n321 20\n2021 589\n962 8523\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "100 100 26\n321 20 131\n2021 589 182\n962 8523 262\n")

    def test_solve_3(self):
        """__test_solve_3"""
        reader = StringIO("632 102\n52 200\n201 130\n666 792\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "632 102 144\n52 200 125\n201 130 125\n666 792 171\n")
# ----
# main
# ----

if __name__ == "__main__":
    main()
