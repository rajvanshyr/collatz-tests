"""TestCollatz"""
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

from Collatz import collatz_read, get_length, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """
    TestCollatz
    """
    # ----
    # read
    # ----

    def test_read_1(self):
        """
        collatz_read
        """
        string = "1 10\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """
        collatz_read
        """
        string = "10000 1\n"
        i, j = collatz_read(string)
        self.assertEqual(i, 10000)
        self.assertEqual(j, 1)

    # ----
    # get_length
    # ----

    def test_get_length_1(self):
        """
        get_length
        """
        value = get_length(1000001)
        self.assertEqual(value, 114)

    def test_get_length_2(self):
        """
        get_length
        """
        value = get_length(1)
        self.assertEqual(value, 1)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """
        collatz_eval
        """
        value = collatz_eval(5, 10)
        self.assertEqual(value, 20)

    def test_eval_2(self):
        """
        collatz_eval
        """
        value = collatz_eval(50, 150)
        self.assertEqual(value, 122)

    def test_eval_3(self):
        """
        collatz_eval
        """
        value = collatz_eval(190, 220)
        self.assertEqual(value, 120)

    def test_eval_4(self):
        """
        collatz_eval
        """
        value = collatz_eval(1000, 900)
        self.assertEqual(value, 174)

    def test_eval_5(self):
        """
        collatz_eval
        """
        value = collatz_eval(10, 1)
        self.assertEqual(value, 20)

    def test_eval_6(self):
        """
        collatz_eval
        """
        value = collatz_eval(1, 1)
        self.assertEqual(value, 1)

    def test_eval_7(self):
        """
        collatz_eval
        """
        value = collatz_eval(999999, 999999)
        self.assertEqual(value, 259)

    # -----
    # print
    # -----

    def test_print_1(self):
        """
        test_print
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        test_print
        """
        writer = StringIO()
        collatz_print(writer, 10, 1, 20)
        self.assertEqual(writer.getvalue(), "10 1 20\n")

    # -----
    # solve
    # -----

    def test_solve(self):
        """
        collatz_solve
        """
        reader = StringIO("1 10\n100 200\n190 220\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n100 200 125\n190 220 120\n900 1000 174\n")

    def test_solve_2(self):
        """
        collatz_solve
        extra blank line
        """
        reader = StringIO("1 10\n\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "1 10 20\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
    
