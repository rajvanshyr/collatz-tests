""" Test Collatz file for public test repo submission """

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
from Collatz import collatz_solve, collatz_eval_individual

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """ Test Collatz class for test harness purposes """

    # ----
    # read
    # ----

    def test_read(self):
        """ read test 1 """
        string_input = "1 10\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 1)
        self.assertEqual(second, 10)

    def test_read2(self):
        """ read test 2 """
        string_input = "100 106\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 100)
        self.assertEqual(second, 106)

    def test_read3(self):
        """ read test 3 """
        string_input = "1000 2000\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 1000)
        self.assertEqual(second, 2000)

    def test_read4(self):
        """ read test 4 """
        string_input = "5 3\n"
        first, second = collatz_read(string_input)
        self.assertEqual(first, 5)
        self.assertEqual(second, 3)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ testing eval: test 1 """
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """ testing eval: test 2 """
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """ testing eval: test 3 """
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """ testing eval: test 4 """
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """ testing eval: test 5 """
        value = collatz_eval(11, 16)
        self.assertEqual(value, 18)

    # -----
    # print
    # -----

    def test_print(self):
        """ testing print: test 1 """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print2(self):
        """ testing print: test 2 """
        writer = StringIO()
        collatz_print(writer, 111, 222, 125)
        self.assertEqual(writer.getvalue(), "111 222 125\n")

    def test_print3(self):
        """ testing print: test 3 """
        writer = StringIO()
        collatz_print(writer, 3048, 4125, 238)
        self.assertEqual(writer.getvalue(), "3048 4125 238\n")

    def test_print4(self):
        """ testing print: test 4 """
        writer = StringIO()
        collatz_print(writer, 1106, 2222, 182)
        self.assertEqual(writer.getvalue(), "1106 2222 182\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """ testing solve collatz: test 1 """
        reader = StringIO("1 999999\n200 100\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "1 999999 396\n200 100 125\n201 210 89\n900 1000 174\n")

    def test_solve2(self):
        """ testing solve collatz: test 2 """
        reader = StringIO("1 3\n132 164\n206 315\n400 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "1 3 8\n132 164 117\n206 315 131\n400 1000 179\n")

    def test_solve3(self):
        """ testing solve collatz: test 3 """
        reader = StringIO("22 26\n1 31\n5 1032\n1113 2246\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "22 26 24\n1 31 112\n5 1032 179\n1113 2246 183\n")

    def test_solve4(self):
        """ testing solve collatz: test 4 """
        reader = StringIO("106 2000\n37 189\n1337 2048\n916 917\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "106 2000 182\n37 189 125\n1337 2048 180\n916 917 37\n")

    # ---------------
    # eval_individual
    # ---------------

    def test_eval_individual(self):
        """ testing eval_individual: test 1 """
        value = collatz_eval_individual(999999)
        self.assertEqual(value, 259)

    def test_eval_individual2(self):
        """ testing eval_individual: test 2 """
        value = collatz_eval_individual(5)
        self.assertEqual(value, 6)

    def test_eval_individual3(self):
        """ testing eval_individual: test 3 """
        value = collatz_eval_individual(20)
        self.assertEqual(value, 8)

# ----
# main
# ----

if __name__ == "__main__":
    main()
