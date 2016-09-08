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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_length

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):
    """
    All test cases
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        Test 1 to see if read
        is correct
        """
        string = "1 10\n"
        minim, maxim = collatz_read(string)
        self.assertEqual(minim, 1)
        self.assertEqual(maxim, 10)

    def test_read_2(self):
        """
        Test 2 to see if read
        is correct
        """
        string = "100 200\n"
        minim, maxim = collatz_read(string)
        self.assertEqual(minim, 100)
        self.assertEqual(maxim, 200)

    def test_read_3(self):
        """
        Test 3 to see if read
        is correct
        """
        string = "100000 200000\n"
        minim, maxim = collatz_read(string)
        self.assertEqual(minim, 100000)
        self.assertEqual(maxim, 200000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        Test 1 to see if
        evaluating correctly
        """
        verify = collatz_eval(1, 10)
        self.assertEqual(verify, 20)

    def test_eval_2(self):
        """
        Test 2 to see if
        evaluating correctly
        """
        verify = collatz_eval(100, 200)
        self.assertEqual(verify, 125)

    def test_eval_3(self):
        """
        Test 3 to see if
        evaluating correctly
        """
        verify = collatz_eval(201, 210)
        self.assertEqual(verify, 89)

    def test_eval_4(self):
        """
        Test 4 to see if
        evaluating correctly
        """
        verify = collatz_eval(900, 1000)
        self.assertEqual(verify, 174)

    # -----
    # print
    # -----

    #Test if print is working
    def test_print_1(self):
        """
        Test 1 to see if
        printing correctly
        """
        write = StringIO()
        collatz_print(write, 1, 10, 20)
        self.assertEqual(write.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Test 2 to see if
        evaluating correctly
        """
        write = StringIO()
        collatz_print(write, 100, 200, 125)
        self.assertEqual(write.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """
        Test 3 to see if
        evaluating correctly
        """
        write = StringIO()
        collatz_print(write, 201, 210, 89)
        self.assertEqual(write.getvalue(), "201 210 89\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Test 1 to see if
        total process  is
        correct
        """
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        Test 2 to see if
        total process  is
        correct
        """
        read = StringIO("54 9000\n234903 950943\n809454 934904\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "54 9000 262\n234903 950943 525\n809454 934904 525\n")

    def test_solve_3(self):
        """
        Test 3 to see if
        total process  is
        correct
        """
        read = StringIO("483 3490\n123 4903\n650 5098\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(), "483 3490 217\n123 4903 238\n650 5098 238\n")
    # -----
    # length
    # -----

    def test_length_1(self):
        """
        Test 1 to see if
        lenth for value is
        correct
        """
        verify = collatz_length(100)
        self.assertEqual(verify, 26)

    def test_length_2(self):
        """
        Test 2 to see if
        lenth for value is
        correct
        """
        verify = collatz_length(43)
        self.assertEqual(verify, 30)

    def test_length_3(self):
        """
        Test 3 to see if
        lenth for value is
        correct
        """
        verify = collatz_length(350)
        self.assertEqual(verify, 82)

# ----
# main
# ----

if __name__ == "__main__":
    main()
