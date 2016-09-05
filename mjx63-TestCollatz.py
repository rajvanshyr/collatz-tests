"""Testing Harness for Collatz project"""
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

from Collatz import collatz_read, get_cycle_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):

    """Contains test methods that test each function in Collatz.py"""
    # ----
    # read
    # ----

    def test_read_1(self):
        """Test collatz_read function"""
        line = "1 10\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """Test collatz_read function"""
        line = "10 20\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 10)
        self.assertEqual(j, 20)

    def test_read_3(self):
        """Test collatz_read function"""
        line = "30 40\n"
        i, j = collatz_read(line)
        self.assertEqual(i, 30)
        self.assertEqual(j, 40)

    #-----------------
    # get_cycle_length
    #-----------------

    def test_get_cycle_length_1(self):
        """Test get_cycle_length function"""
        num = 30
        result = get_cycle_length(num)
        self.assertEqual(result, 19)

    def test_get_cycle_length_2(self):
        """Test get_cycle_length function"""
        num = 50
        result = get_cycle_length(num)
        self.assertEqual(result, 25)

    def test_get_cycle_length_3(self):
        """Test get_cycle_length function"""
        num = 100
        result = get_cycle_length(num)
        self.assertEqual(result, 26)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test collatz_eval function"""
        value = collatz_eval(1, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """Test collatz_eval function"""
        value = collatz_eval(100, 200)
        self.assertEqual(value, 125)

    def test_eval_3(self):
        """Test collatz_eval function"""
        value = collatz_eval(201, 210)
        self.assertEqual(value, 89)

    def test_eval_4(self):
        """Test collatz_eval function"""
        value = collatz_eval(900, 1000)
        self.assertEqual(value, 174)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test collatz_print function"""
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """Test collatz_print function"""
        writer = StringIO()
        collatz_print(writer, 10, 20, 30)
        self.assertEqual(writer.getvalue(), "10 20 30\n")

    def test_print_3(self):
        """Test collatz_print function"""
        writer = StringIO()
        collatz_print(writer, 30, 40, 50)
        self.assertEqual(writer.getvalue(), "30 40 50\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test collatz_solve function"""
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """Test collatz_solve function"""
        reader = StringIO("1 1\n358346 358846\n280576 284136\n113384 134378\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), \
            "1 1 1\n358346 358846 348\n280576 284136 358\n113384 134378 349\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
