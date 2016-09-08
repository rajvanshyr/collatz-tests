""" Jake Mayo Fall 2016 Test Harness """
#!/usr/bin/envalpython3

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
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, find_3n, correct_input

# -----------
# TestCollatz
# -----------

class TestCollatz(TestCase):

    """ test collatz """
    # ----
    # read
    # ----

    def test_read_1(self):
        """ test collatz_read """
        string = "1 10\n"
        val_1, val_2 = collatz_read(string)
        self.assertEqual(val_1, 1)
        self.assertEqual(val_2, 10)

    def test_read_2(self):
        """ test collatz_read """
        string = "40 67\n"
        val_1, val_2 = collatz_read(string)
        self.assertEqual(val_1, 40)
        self.assertEqual(val_2, 67)

    def test_read_3(self):
        """ test collatz_read """
        string = "100 45000\n"
        val_1, val_2 = collatz_read(string)
        self.assertEqual(val_1, 100)
        self.assertEqual(val_2, 45000)

    # ----
    # eval
    # ----

    def test_eval_1(self):
        """ test eval """
        val = collatz_eval(1, 10)
        self.assertEqual(val, 20)

    def test_eval_2(self):
        """ test eval """
        val = collatz_eval(100, 200)
        self.assertEqual(val, 125)

    def test_eval_3(self):
        """ test eval """
        val = collatz_eval(201, 210)
        self.assertEqual(val, 89)

    # -----
    # print
    # -----

    def test_print_1(self):
        """ test print """
        doc = StringIO()
        collatz_print(doc, 1, 10, 20)
        self.assertEqual(doc.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """ test print """
        doc = StringIO()
        collatz_print(doc, 100, 200, 125)
        self.assertEqual(doc.getvalue(), "100 200 125\n")

    def test_print_3(self):
        """ test print """
        doc = StringIO()
        collatz_print(doc, 500, 500, 111)
        self.assertEqual(doc.getvalue(), "500 500 111\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """ test solve """
        string_in = StringIO("10 1\n251 500\n201 210\n737959 737959\n")
        doc = StringIO()
        collatz_solve(string_in, doc)
        self.assertEqual(
            doc.getvalue(),
            "10 1 20\n251 500 144\n201 210 89\n737959 737959 142\n")

    def test_solve_2(self):
        """ test solve """
        string_in = StringIO("57893 81883\n78 179\n5 69917\n")
        doc = StringIO()
        collatz_solve(string_in, doc)
        self.assertEqual(
            doc.getvalue(),
            "57893 81883 351\n78 179 125\n5 69917 340\n")

    def test_solve_3(self):
        """ test solve """
        string_in = StringIO("729 69823\n353 406\n782 34624\n")
        doc = StringIO()
        collatz_solve(string_in, doc)
        self.assertEqual(
            doc.getvalue(),
            "729 69823 340\n353 406 126\n782 34624 311\n")

    def test_solve_4(self):
        """ test solve """
        string_in = StringIO("38621 71429\n45833 79135\n1 499\n")
        doc = StringIO()
        collatz_solve(string_in, doc)
        self.assertEqual(
            doc.getvalue(),
            "38621 71429 340\n45833 79135 351\n1 499 144\n")

    # -----
    # find_3n
    # -----

    def test_find_3n_1(self):
        """ test cycle of n"""
        val = find_3n(100)
        self.assertEqual(val, 26)

    def test_find_3n_2(self):
        """ test cycle of n """
        val = find_3n(999)
        self.assertEqual(val, 50)

    def test_find_3n_3(self):
        """ test cycle of n """
        val = find_3n(101101)
        self.assertEqual(val, 67)

    # -----
    # correct_input
    # -----

    def test_correct_input_1(self):
        """ test correct input """
        val = correct_input("test test")
        self.assertEqual(val, False)

    def test_correct_input_2(self):
        """ test correct input """
        val = correct_input("1 2")
        self.assertEqual(val, True)

    def test_correct_input_3(self):
        """ test correct input """
        val = correct_input("1 2 3")
        self.assertEqual(val, False)

    def test_correct_input_4(self):
        """ test correct input """
        val = correct_input("0 1000005")
        self.assertEqual(val, False)

# ----
# main
# ----

if __name__ == "__main__":
    main()
