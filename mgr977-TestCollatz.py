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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc, collatz_calc_r, cache_lookup, cache_flush

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        string = "1 10\n"
        valueOne, valueTwo = collatz_read(string)
        self.assertEqual(valueOne,  1)
        self.assertEqual(valueTwo, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        result = collatz_eval(1, 10)
        self.assertEqual(result, 20)

    def test_eval_2(self):
        result = collatz_eval(100, 200)
        self.assertEqual(result, 125)

    def test_eval_3(self):
        result = collatz_eval(201, 210)
        self.assertEqual(result, 89)

    def test_eval_4(self):
        result = collatz_eval(900, 1000)
        self.assertEqual(result, 174)

    # ----
    # calc
    # ----

    def test_calc_1(self):
        result = collatz_calc(1)
        self.assertEqual(result, 1)

    def test_calc_2(self):
        result = collatz_calc(2)
        self.assertEqual(result, 2)

    def test_calc_3(self):
        result = collatz_calc(3)
        self.assertEqual(result, 8)

    def test_calc_27(self):
        result = collatz_calc(27)
        self.assertEqual(result, 112)

    def test_calc_500(self):
        result = collatz_calc(500)
        self.assertEqual(result, 111)

    def test_calc_r_1(self):
        result = collatz_calc_r(1, 0)
        self.assertEqual(result, 1)

    def test_calc_r_2(self):
        result = collatz_calc_r(2, 0)
        self.assertEqual(result, 2)

    def test_calc_r_3(self):
        result = collatz_calc_r(3, 0)
        self.assertEqual(result, 8)

    def test_calc_r_27(self):
        result = collatz_calc_r(27, 0)
        self.assertEqual(result, 112)

    def test_calc_r_500(self):
        result = collatz_calc_r(500, 0)
        self.assertEqual(result, 111)

    # general does the cache work test
    def test_cache_1(self):
        cache_flush()
        collatz_calc(4)
        self.assertEqual(cache_lookup(4), 3)
        self.assertEqual(cache_lookup(2), 2)
        self.assertEqual(cache_lookup(100), 0)

    # test whether cache maintains cached items from a previous problem
    def test_cache_2(self):
        cache_flush()
        collatz_calc(113)
        self.assertEqual(cache_lookup(85), 10)
        collatz_calc(500)
        self.assertEqual(cache_lookup(53), 12)
        self.assertEqual(cache_lookup(15), 0)

    def test_cache_3(self):
        cache_flush()
        self.assertEqual(cache_lookup(collatz_calc(12)), 7)

    def test_cache_4(self):
        collatz_calc(2)
        cache_flush()
        self.assertEqual(cache_lookup(2), 0)

    # reverse input
    # def test_eval(self):
     #   self.assertEqual(collatz_eval(40, 1), 112)

    # -----
    # print
    # -----
    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
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
