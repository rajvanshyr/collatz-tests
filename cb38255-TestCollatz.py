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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, get_cycle


# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2 (self) :
        s    = "999999 1000000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  999999)
        self.assertEqual(j, 1000000)

    def test_read3 (self) :
        s    = "234 345\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  234)
        self.assertEqual(j, 345)

    def test_read4 (self) :
        s    = "11111 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  11111)
        self.assertEqual(j, 10)

    # ----
    # eval
    # ----

    def test_eval1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval2 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval5 (self) :
        v = collatz_eval(9002, 123345)
        self.assertEqual(v, 354)

    def test_eval6 (self) :
        v = collatz_eval(99853, 785345)
        self.assertEqual(v, 509)

    def test_eval7 (self) :
        v = collatz_eval(728222, 23)
        self.assertEqual(v, 509)

    # -----
    # print
    # -----

    def test_print1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 1, 100, 119)
        self.assertEqual(w.getvalue(), "1 100 119\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 23832, 23234, 284)
        self.assertEqual(w.getvalue(), "23832 23234 284\n")

    # -----
    # solve
    # -----

    def test_solve11 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self):
        read = StringIO("491 2460\n950 2853\n325 1296\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(
            write.getvalue(), "491 2460 183\n950 2853 209\n325 1296 182\n")

    def test_solve3 (self):
        reader = StringIO("1 1\n8493 358846\n8473 27\n11234 1378\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), \
            "1 1 1\n8493 358846 443\n8473 27 262\n11234 1378 268\n")

    # ----
    # get_cycle
    # ----

    def test_get1 (self):
        """Does get_cycle work?"""
        num = 5
        length = get_cycle(num)
        self.assertEqual(length, 6)

    def test_get2 (self):
        num = 1000000
        length = get_cycle(num)
        self.assertEqual(length, 153)

    def test_get3 (self):
        num = 3343
        length = get_cycle(num)
        self.assertEqual(length, 44)

    # ----
    # main
    # ----

if __name__ == "__main__" :
    main()
