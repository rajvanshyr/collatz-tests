'''
    This module provides unit tests for functions in Collatz.
'''
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_single

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    '''
        TestCollatz serves as our class to hold unit test methods
        to test functions in Collatz.
    '''
    # ----
    # read
    # ----

    def test_read(self):
        '''
            Test the collatz_read() function which takes in a string
            containing two integers and should return the two integers
            in integer form.
        '''
        string_input = "1 10\n"
        start_range, end_range = collatz_read(string_input)
        self.assertEqual(start_range, 1)
        self.assertEqual(end_range, 10)

    def test_read_2(self):
        '''
            Test the collatz_read() function which takes in a string
            containing two integers and should return the two integers
            in integer form.
        '''
        string_input = "10 1\n"
        start_range, end_range = collatz_read(string_input)
        self.assertEqual(start_range, 10)
        self.assertEqual(end_range, 1)

    def test_read_3(self):
        '''
            Test the collatz_read() function which takes in a string
            containing two integers and should return the two integers
            in integer form.
        '''
        string_input = "500000 0\n"
        start_range, end_range = collatz_read(string_input)
        self.assertEqual(start_range, 500000)
        self.assertEqual(end_range, 0)

    def test_read_4(self):
        '''
            Test the collatz_read() function which takes in a string
            containing two integers and should return the two integers
            in integer form.
        '''
        string_input = "5 6\n"
        start_range, end_range = collatz_read(string_input)
        self.assertEqual(start_range, 5)
        self.assertEqual(end_range, 6)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        '''
            Test the collatz_eval() function with range [1, 10].
        '''
        collatz_eval_result = collatz_eval(1, 10)
        self.assertEqual(collatz_eval_result, 20)

    def test_eval_2(self):
        '''
            Test the collatz_eval() function with range [100, 200].
        '''
        collatz_eval_result = collatz_eval(100, 200)
        self.assertEqual(collatz_eval_result, 125)

    def test_eval_3(self):
        '''
            Test the collatz_eval() function with range [201, 210].
        '''
        collatz_eval_result = collatz_eval(201, 210)
        self.assertEqual(collatz_eval_result, 89)

    def test_eval_4(self):
        '''
            Test the collatz_eval() function with range [900, 1000].
        '''
        collatz_eval_result = collatz_eval(900, 1000)
        self.assertEqual(collatz_eval_result, 174)

    # ----
    # eval
    # ----

    def test_single_1(self):
        '''
            Test the collatz_single() function with value 10.
        '''
        cycle_result = collatz_single(10)
        self.assertEqual(cycle_result, 7)

    def test_single_2(self):
        '''
            Test the collatz_single() function with value 5.
        '''
        cycle_result = collatz_single(5)
        self.assertEqual(cycle_result, 6)

    def test_single_3(self):
        '''
            Test the collatz_single() function with value 1.
        '''
        cycle_result = collatz_single(1)
        self.assertEqual(cycle_result, 1)

    # -----
    # print
    # -----

    def test_print(self):
        '''
            Testing the collatz_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        collatz_print(write_io, 1, 10, 20)
        self.assertEqual(write_io.getvalue(), "1 10 20\n")

    def test_print_2(self):
        '''
            Testing the collatz_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        collatz_print(write_io, 10, 1, 20)
        self.assertEqual(write_io.getvalue(), "10 1 20\n")

    def test_print_3(self):
        '''
            Testing the collatz_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        collatz_print(write_io, 1, 1, 1)
        self.assertEqual(write_io.getvalue(), "1 1 1\n")

    def test_print_4(self):
        '''
            Testing the collatz_print() function by passing a StringIO
            object to write to instead of standard out.
        '''
        write_io = StringIO()
        collatz_print(write_io, 1, 2, 2)
        self.assertEqual(write_io.getvalue(), "1 2 2\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        '''
            Testing the collatz_solve() function with the ranges:
            [1, 10], [100, 200], [201, 210], [900, 1000]. We are
            passing a StringIO object in place of standard input.
        '''
        read_io = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write_io = StringIO()
        collatz_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        '''
            Testing the collatz_solve() function with the range [1, 1]
        '''
        read_io = StringIO("1 1\n")
        write_io = StringIO()
        collatz_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "1 1 1\n")

    def test_solve_3(self):
        '''
            Testing the collatz_solve() function with the range [1, 10]
        '''
        read_io = StringIO("10 1\n")
        write_io = StringIO()
        collatz_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "10 1 20\n")

    def test_solve_4(self):
        '''
            Testing the collatz_solve() function with the range [5, 5]
        '''
        read_io = StringIO("900 9597\n")
        write_io = StringIO()
        collatz_solve(read_io, write_io)
        self.assertEqual(write_io.getvalue(), "900 9597 262\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
