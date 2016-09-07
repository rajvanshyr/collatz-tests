"""Test Collatz"""
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calculate

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    Class for testing Collatz
    """
    # ----
    # read
    # ----

    def test_read(self):
        """ Ensure that input string is read and parsed correctly """
        s_value = "1 10\n"
        i_value, j_value = collatz_read(s_value)
        self.assertEqual(i_value, 1)
        self.assertEqual(j_value, 10)

    # ----
    # calculate
    # ----

    def test_calculate_1(self):
        """
        Ensure calculate functionality is correct
        """
        c_value = collatz_calculate(10)
        self.assertEqual(c_value, 7)

    def test_calculate_2(self):
        """
        Ensure calculate functionality is correct
        """
        c_value = collatz_calculate(20000)
        self.assertEqual(c_value, 31)

    def test_calculate_3(self):
        """
        Ensure calculate functionality is correct
        """
        c_value = collatz_calculate(1500)
        self.assertEqual(c_value, 48)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Ensure eval functionality is correct
        """
        v_value = collatz_eval(1, 10)
        self.assertEqual(v_value, 20)

    def test_eval_2(self):
        """
        Ensure eval functionality is correct
        """
        v_value = collatz_eval(100, 200)
        self.assertEqual(v_value, 125)

    def test_eval_3(self):
        """
        Ensure eval functionality is correct
        """
        v_value = collatz_eval(201, 210)
        self.assertEqual(v_value, 89)

    def test_eval_4(self):
        """
        Ensure eval functionality is correct
        """
        v_value = collatz_eval(900, 1000)
        self.assertEqual(v_value, 174)

    def test_eval_5(self):
        """
        Make sure even range in the wrong order works
        """
        v_value = collatz_eval(1000, 900)
        self.assertEqual(v_value, 174)

    def test_eval_6(self):
        """
        Make sure even range in the wrong order works
        """
        v_value = collatz_eval(210, 201)
        self.assertEqual(v_value, 89)

    def test_eval_7(self):
        """
        Make sure even range in the wrong order works
        """
        v_value = collatz_eval(10, 1)
        self.assertEqual(v_value, 20)

    def test_eval_8(self):
        """
        Test the b < m and m = e/2 + 1 then mcl(b,e) = mcl(m,e)
        """
        v_value = collatz_eval(10, 100)
        self.assertEqual(v_value, 119)

    def test_eval_9(self):
        """
        Test the b < m and m = e/2 + 1 then mcl(b,e) = mcl(m,e)
        """
        v_value = collatz_eval(1, 348)
        self.assertEqual(v_value, 144)

    def test_eval_10(self):
        """
        Test the b < m and m = e/2 + 1 then mcl(b,e) = mcl(m,e)
        """
        v_value = collatz_eval(18, 20)
        self.assertEqual(v_value, 21)

    # -----
    # print
    # -----

    def test_print(self):
        """ Ensure print functionality is correct """
        w_value = StringIO()
        collatz_print(w_value, 1, 10, 20)
        self.assertEqual(w_value.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """ Ensure solve functionality is correct """
        r_value = StringIO("1 10\n100 200\n201 210\n900 1000\n1000 900\n")
        w_value = StringIO()
        collatz_solve(r_value, w_value)
        self.assertEqual(
            w_value.getvalue(),
            "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n1000 900 174\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
