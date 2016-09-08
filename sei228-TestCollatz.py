#!/usr/bin/env python3

"""
projects/collatz/TestCollatz.py
Copyright (C) 2016
Glenn P. Downing
"""

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
    """
    test for Collatz module
    """

    # ----
    # read
    # ----

    def test_read_1(self):
        """
        simple read
        """
        string = "1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """
        simple read
        """
        string = "-1 10\n"
        start, end = collatz_read(string)
        self.assertEqual(start, -1)
        self.assertEqual(end, 10)

    # ----
    # cycle_length
    # ----

    def test_cycle_length_1(self):
        """
        simple cycle length test
        """
        length = collatz_cycle_length(40)
        self.assertEqual(length, 9)

    def test_cycle_length_2(self):
        """
        simple cycle length test
        """
        length = collatz_cycle_length(20)
        self.assertEqual(length, 8)

    def test_cycle_length_3(self):
        """
        simple cycle length test
        """
        length = collatz_cycle_length(999)
        self.assertEqual(length, 50)

    def test_cycle_length_4(self):
        """
        simple cycle length test
        """
        length = collatz_cycle_length(790)
        self.assertEqual(length, 78)

    def test_cycle_length_5(self):
        """
        simple cycle length test
        """
        length = collatz_cycle_length(5)
        self.assertEqual(length, 6)
    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        simple eval test
        """
        length = collatz_eval(1, 10)
        self.assertEqual(length, 20)

    def test_eval_2(self):
        """
        simple eval test
        """
        length = collatz_eval(100, 200)
        self.assertEqual(length, 125)

    def test_eval_3(self):
        """
        simple eval test
        """
        length = collatz_eval(201, 210)
        self.assertEqual(length, 89)

    def test_eval_4(self):
        """
        simple eval test
        """
        length = collatz_eval(900, 1000)
        self.assertEqual(length, 174)

    def test_eval_5(self):
        """
        simple eval test
        """
        length = collatz_eval(1, 2)
        self.assertEqual(length, 2)

    def test_eval_6(self):
        """
        simple eval test
        """
        length = collatz_eval(10000, 10000)
        self.assertEqual(length, 30)

    def test_eval_7(self):
        """
        simple eval test
        """
        length = collatz_eval(100000, 100000)
        self.assertEqual(length, 129)

    def test_eval_8(self):
        """
        sphere has bounds the wrong way around sometimes.
        """
        length = collatz_eval(10, 1)
        self.assertEqual(length, 20)

    # -----
    # print
    # -----

    def test_print(self):
        """
        simple print test
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        simple solve test
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
