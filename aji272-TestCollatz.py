"""Alex Irion 2016 - Testing Class"""
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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, cycle_len

# -----------
# TestCollatz
# -----------
class TestCollatz(TestCase):
    """
    Collatz testing class
    """

    # ----
    # read
    # ----
    def test_read_1(self):
        """
        read 1
        """
        begin, end = collatz_read("1 10\n")
        self.assertEqual(begin, 1)
        self.assertEqual(end, 10)

    def test_read_2(self):
        """
        read 2
        """
        begin, end = collatz_read("111 555\n")
        self.assertEqual(begin, 111)
        self.assertEqual(end, 555)

    def test_read_3(self):
        """
        read 3
        """
        begin, end = collatz_read("10 11\n")
        self.assertEqual(begin, 10)
        self.assertEqual(end, 11)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        """
        eval 1
        """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """
        eval 2
        """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """
        eval 3
        """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    def test_eval_4(self):
        """
        eval 4
        """
        self.assertEqual(174, collatz_eval(1000, 900))

    def test_eval_5(self):
        """
        eval 5
        """
        val = collatz_eval(900, 1000)
        self.assertEqual(val, 174)

    # ---
    # cycle_len
    # ---
    def test_cycle_len_1(self):
        """
        cycle_len 1
        """
        self.assertEqual(7, cycle_len(10))

    def test_cycle_len_2(self):
        """
        cycle_len 2
        """
        self.assertEqual(31, cycle_len(555))

    def test_cycle_len_3(self):
        """
        cycle_len 3
        """
        self.assertEqual(55, cycle_len(956))

    def test_cycle_len_4(self):
        """
        cycle_len 4
        """
        self.assertEqual(26, cycle_len(101))


    # -----
    # print
    # -----
    def test_print_1(self):
        """
        print 1
        """
        writer = StringIO()
        collatz_print(writer, 44, 575, 9389)
        self.assertEqual(writer.getvalue(), "44 575 9389\n")

    def test_print_2(self):
        """
        print 2
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_3(self):
        """
        print 3
        """
        writer = StringIO()
        collatz_print(writer, 738, 10, 400)
        self.assertEqual(writer.getvalue(), "738 10 400\n")

    # -----
    # solve
    # -----
    def test_solve_1(self):
        """
        solve 1
        """
        reader = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        solve 2
        """
        reader = StringIO("1000 900\n1252 2252\n2252 3252")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "1000 900 174\n1252 2252 183\n2252 3252 217\n")

    def test_solve_3(self):
        """
        solve 3
        """
        reader = StringIO("2 1\n7252 8252\n6252 7252\n4252 5252\n")
        writer = StringIO()
        collatz_solve(reader, writer)
        self.assertEqual(writer.getvalue(), "2 1 2\n7252 8252 252\n6252 7252 257\n4252 5252 215\n")

# ----
# main
# ----

if __name__ == "__main__":
    main()
