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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_length, apply_to_cache

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    # ----
    # read
    # ----

    def test_read(self):
        read_in = "1 10\n"
        begin, end = collatz_read(read_in)
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        val = collatz_eval(1000, 900)
        self.assertEqual(val, 174)

    # -----
    # print
    # -----

    def test_print(self):
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    # --------------
    # apply_to_cache
    # --------------
    
    def test_apply_to_cache_1(self):
        cache = [0, 14, 45]
        cache_dict = {0: 5}
        apply_to_cache(cache, cache_dict, 100)
        self.assertEqual(cache[0], 95)

    def test_apply_to_cache_2(self):
        cache = [0] * 100
        cache_dict = {99: 99, 34: 12}
        expected_cache = [0] * 100
        expected_cache[99] = 1
        expected_cache[34] = 88
        apply_to_cache(cache, cache_dict, 100)
        self.assertEqual(cache, expected_cache)

    def test_apply_to_cache_3(self):
        cache = [123, 4, 0, 0, 0, 0]
        cache_dict = {5: 1, 2: 9, 4: 3}
        apply_to_cache(cache, cache_dict, 10)
        self.assertEqual(cache, [123, 4, 1, 0, 7, 9])

    # ------------
    # cycle_length
    # ------------

    def test_cycle_length_1(self):
        res = cycle_length(1, [0, 0])
        self.assertEqual(res, 1)

    def test_cycle_length_2(self):
        res = cycle_length(32, [0] * 33)
        self.assertEqual(res, 6)

    def test_cycle_length_3(self):
        res = cycle_length(17, [0]*18)
        self.assertEqual(res, 13)

    # Test cache capability
    def test_cycle_length_4(self):
        cache = [0]*18
        cycle_length(9, cache)
        self.assertEqual(cache[9], 20)

    # Test cache capability
    def test_cycle_length_5(self):
        cache = [0]*18
        cycle_length(9, cache)
        self.assertEqual(cache[7], 17)

    # -----
    # solve
    # -----

    def test_solve_1(self):
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        reader = StringIO("10 1\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "10 1 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_3(self):
        reader = StringIO("1 10\n100 200\n201 210\n950 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(),
            "1 10 20\n100 200 125\n201 210 89\n950 1000 143\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
