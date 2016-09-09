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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self):
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_1 (self):
        s = "59 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 59)
        self.assertEqual(j, 1000)

    def test_read_2 (self):
        s = "123456 987654\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 123456)

    def test_read_3 (self):
        s = "42 24\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 42)
        self.assertEqual(j, 24)

    #------------
    #cycle_length
    #------------
    def test_cycle_length_1(self):
        c = collatz_cycle_length(5)
        self.assertEqual(6, c)

    def test_cycle_length_2(self):
        c = collatz_cycle_length(1234)
        self.assertEqual(133, c)

    def test_cycle_length_3(self):
        c = collatz_cycle_length(3001)
        self.assertEqual(41, c)

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

    def test_eval_5 (self):
        v = collatz_eval(1, 7)
        self.assertEqual(v, 17)

    def test_eval_6 (self):
        v = collatz_eval(1000, 1013)
        self.assertEqual(v, 143)

    def test_eval_7 (self):
        v = collatz_eval(3, 12)
        self.assertEqual(v, 20)

    def test_eval_8 (self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_9 (self):
        v = collatz_eval(1000000, 1000000)
        self.assertEqual(v, 153)

    # -----
    # print
    # -----

    def test_print (self):
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_1 (self):
        w = StringIO()
        collatz_print(w, 5, 121, 32)
        self.assertEqual(w.getvalue(), "5 121 32\n")


    def test_print_2 (self):
        w = StringIO()
        collatz_print(w, 1000, 1013, 142)
        self.assertEqual(w.getvalue(), "1000 1013 142\n")
    # -----
    # solve
    # -----

    def test_solve (self):
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_1 (self):
        r = StringIO("1 1\n1000 1013\n1 13\n1000000 1000000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1000 1013 143\n1 13 20\n1000000 1000000 153\n")

    def test_solve_2 (self):
        r = StringIO("3 12\n1 7\n1 13\n41 45\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "3 12 20\n1 7 17\n1 13 20\n41 45 110\n")
# ----
# main
# ----

if __name__ == "__main__" :
    main()
