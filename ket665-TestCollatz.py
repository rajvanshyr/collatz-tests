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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read2 (self) :
        s    = "4 16\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  4)
        self.assertEqual(j, 16)

    def test_read (self) :
        s    = "87 936\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  87)
        self.assertEqual(j, 936)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)

    def test_eval_7 (self) :
        v = collatz_eval(3, 3)
        self.assertEqual(v, 8)

    def test_eval_8 (self) :
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

    def test_eval_9 (self) :
        v = collatz_eval(10, 10)
        self.assertEqual(v, 7)

    def test_eval_10 (self) :
        v = collatz_eval(9, 6)
        self.assertEqual(v, 20)

    def test_eval_11 (self) :
        v = collatz_eval(7, 7)
        self.assertEqual(v, 17)

    def test_eval_12 (self) :
        v = collatz_eval(6, 6)
        self.assertEqual(v, 9)

    def test_eval_13 (self) :
        v = collatz_eval(27, 27)
        self.assertEqual(v, 112)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 6, 6, 9)
        self.assertEqual(w.getvalue(), "6 6 9\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 108, 108, 114)
        self.assertEqual(w.getvalue(), "108 108 114\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 1\n2 2\n3 3\n5 5\n10 10\n9 9\n7 7\n6 6\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n3 3 8\n5 5 6\n10 10 7\n9 9 20\n7 7 17\n6 6 9\n")

    def test_solve_3 (self) :
        r = StringIO("100 171\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "100 171 125\n201 210 89\n900 1000 174\n")

# ----
# main 
# ----

if __name__ == "__main__" :
    main()
