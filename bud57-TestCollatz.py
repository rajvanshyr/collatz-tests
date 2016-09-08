#!/usr/bin/env python3
"""Unit tests for Collatz.py"""

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, do_collatz

# -----------
# TestCollatz
# -----------


class TestCollatz(TestCase):
    """Unit tests for Colatz.py"""

    # ----
    # read
    # ----

    def test_read_1(self):
        """Test collatz_read"""
        string = "1 10\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 1)
        self.assertEqual(input_j, 10)

    def test_read_2(self):
        """Test collatz_read"""
        string = "1000000 0\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 1000000)
        self.assertEqual(input_j, 0)

    def test_read_3(self):
        """Test collatz_read"""
        string = "800 800\n"
        input_i, input_j = collatz_read(string)
        self.assertEqual(input_i, 800)
        self.assertEqual(input_j, 800)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """Test collatz_eval"""
        val = collatz_eval(0, 1000000)
        self.assertEqual(val, 525)

    def test_eval_2(self):
        """Test collatz_eval"""
        val = collatz_eval(64, 47)
        self.assertEqual(val, 113)

    def test_eval_3(self):
        """Test collatz_eval"""
        val = collatz_eval(5, 5)
        self.assertEqual(val, 6)

    def test_eval_4(self):
        """Test collatz_eval"""
        val = collatz_eval(2345, 458)
        self.assertEqual(val, 183)

    # ----------
    # do_collatz
    # ----------

    def test_do_collatz_1(self):
        """Test do_collatz"""
        max_len = do_collatz(23457, 23457)
        self.assertEqual(max_len, 251)

    def test_do_collatz_2(self):
        """Test do_collatz"""
        max_len = do_collatz(980, 1002)
        self.assertEqual(max_len, 143)

    def test_do_collatz_3(self):
        """Test do_collatz"""
        max_len = do_collatz(90900, 90914)
        self.assertEqual(max_len, 271)

    # -----
    # print
    # -----

    def test_print_1(self):
        """Test collatz_print"""
        writer = StringIO()
        collatz_print(writer, 540460, 736383, 509)
        self.assertEqual(writer.getvalue(), "540460 736383 509\n")

    def test_print_2(self):
        """Test collatz_print"""
        writer = StringIO()
        collatz_print(writer, 487845, 812, 449)
        self.assertEqual(writer.getvalue(), "487845 812 449\n")

    def test_print_3(self):
        """Test collatz_print"""
        writer = StringIO()
        collatz_print(writer, 86, 865225, 525)
        self.assertEqual(writer.getvalue(), "86 865225 525\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """Test collatz_solve"""
        reader = StringIO("932297 769796\n 3716 526456\n 27864 9\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(),
                         "932297 769796 525\n3716 526456 470\n27864 9 308\n")

    def test_solve_2(self):
        """Test collatz_solve"""
        reader = StringIO("711851 87792\n 440021 658509\n 71258 231579\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "711851 87792 509\n440021 658509 509\n71258 231579 443\n")

    def test_solve_3(self):
        """Test collatz_solve"""
        reader = StringIO("386724 366039\n458 4598\n135298 192870\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(
            writer.getvalue(), "386724 366039 423\n458 4598 238\n135298 192870 383\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
