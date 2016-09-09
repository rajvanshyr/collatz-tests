#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

"""
    Tests Collatz.py
"""

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
        Tests Collatz.py
    """
    # ----
    # read
    # ----

    def test_read(self):
        """
            Tests read using example values from SPOJ
        """
        s_in = "1 10\n"
        i, j = collatz_read(s_in)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """
            Tests read using example values from SPOJ reversed
        """
        s_in = "10 1\n"
        i, j = collatz_read(s_in)
        self.assertEqual(i, 10)
        self.assertEqual(j, 1)

    def test_read_3(self):
        """
            Tests read using random numbers
        """
        s_in = "1412 4869\n"
        i, j = collatz_read(s_in)
        self.assertEqual(i, 1412)
        self.assertEqual(j, 4869)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
            Tests eval using example values from SPOJ
        """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """
            Tests eval using example values from SPOJ
        """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """
            Tests eval using example values from SPOJ
        """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """
            Tests eval using example values from SPOJ
        """
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    def test_eval_5(self):
        """
            Tests eval using example values from SPOJ reversed
        """
        val = collatz_eval(1000, 900)
        self.assertEqual(val, 174)

    def test_eval_6(self):
        """
            Tests eval using example values from SPOJ reversed
        """
        val = collatz_eval(10, 1)
        self.assertEqual(val, 20)

    def test_eval_7(self):
        """
            Tests eval using large span, it should run fast
            because it calls the meta_cache version
        """
        val = collatz_eval(940640, 95974)
        self.assertEqual(val, 525)

    # ----
    # eval
    # ----

    def test_eval_10(self):
        """
            Tests eval with the max being 1000000
            because that is handled differently in the code
        """
        val = collatz_eval(990000, 1000000)
        self.assertEqual(val, 440)

    def test_eval_12(self):
        """
            Tests eval where it should get a value
            from the beginning block as the max cycle
        """
        val = collatz_eval(694593, 696001)
        self.assertEqual(val, 367)

    def test_eval_13(self):
        """
            Tests eval where it should get a value
            from the end block as the max cycle
        """
        val = collatz_eval(694999, 698900)
        self.assertEqual(val, 367)

    def test_eval_14(self):
        """
            Tests eval where it should get a value
            from a central block as the max cycle
        """
        val = collatz_eval(694999, 698000)
        self.assertEqual(val, 336)

    def test_eval_15(self):
        """
            Tests eval where it should get a value
            from a central block as the max cycle
        """
        val = collatz_eval(694999, 699000)
        self.assertEqual(val, 367)

    # -----
    # print
    # -----

    def test_print(self):
        """
            Tests printing of rows
        """
        w_out = StringIO()
        collatz_print(w_out, 1, 10, 20)
        self.assertEqual(w_out.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
            Tests printing of rows
            (does not need to be valid collatz values)
        """
        w_out = StringIO()
        collatz_print(w_out, 324134, 12351, 23623452)
        self.assertEqual(w_out.getvalue(), "324134 12351 23623452\n")

    def test_print_3(self):
        """
            Tests printing of rows
            (does not ned to be valid collatz values)
        """
        w_out = StringIO()
        collatz_print(w_out, 31, 10, 0)
        self.assertEqual(w_out.getvalue(), "31 10 0\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
            Tests solve using example values from SPOJ
        """
        r_in = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w_out = StringIO()
        collatz_solve(r_in, w_out)
        self.assertEqual(w_out.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
            Tests solve using example values from SPOJ
            reversed
        """
        r_in = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w_out = StringIO()
        collatz_solve(r_in, w_out)
        self.assertEqual(w_out.getvalue(),
                         "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    def test_solve_3(self):
        """
            Tests solve using example values from SPOJ
            reversed and unreveresed
        """
        r_in = StringIO(
            "10 1\n200 100\n1 10\n100 200\n201 210\n900 1000\n210 201\n1000 900\n")
        w_out = StringIO()
        collatz_solve(r_in, w_out)
        self.assertEqual(w_out.getvalue(),
                         "10 1 20\n200 100 125\n1 10 20\n100 200 125\n201 210 89\n900 1000 174\n210 201 89\n1000 900 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
