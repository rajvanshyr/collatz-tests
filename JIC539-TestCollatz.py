"""This module is the test harness with all unit tests"""
# !/usr/bin/env python3

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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, \
    collatz_eval_not_precached, check_range, one_cycle_length


# -----------
# TestCollatz
# -----------
class TestCollatz(TestCase):
    """
    class will be responsible for the entire test harness via its methods
    """

    # ----
    # read
    # ----
    def test_read_1(self):
        """
        Method will ensure reading is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        input_string = "1 10\n"
        i, j = collatz_read(input_string)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2(self):
        """
        Method will ensure reading is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        input_string = "100 10\n"
        i, j = collatz_read(input_string)
        self.assertEqual(i, 100)
        self.assertEqual(j, 10)

    def test_read_3(self):
        """
        Method will ensure reading is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        input_string = "5555 11110\n"
        i, j = collatz_read(input_string)
        self.assertEqual(i, 5555)
        self.assertEqual(j, 11110)

    def test_read_4(self):
        """
        Method will ensure reading is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        input_string = "        5555        11110\n"
        i, j = collatz_read(input_string)
        self.assertEqual(i, 5555)
        self.assertEqual(j, 11110)

    # ----
    # eval
    # ----
    def test_eval_1(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(1, 10)
        self.assertEqual(returned_val, 20)

    def test_eval_2(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(100, 200)
        self.assertEqual(returned_val, 125)

    def test_eval_3(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(201, 210)
        self.assertEqual(returned_val, 89)

    def test_eval_4(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(900, 1000)
        self.assertEqual(returned_val, 174)

    def test_eval_5(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(10, 1)
        self.assertEqual(returned_val, 20)

    def test_eval_6(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(200, 100)
        self.assertEqual(returned_val, 125)

    def test_eval_7(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(210, 201)
        self.assertEqual(returned_val, 89)

    def test_eval_8(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(1000, 900)
        self.assertEqual(returned_val, 174)

    def test_eval_10(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval(1, 2)
        self.assertEqual(returned_val, 2)

    # ------------------
    # eval_not_precached
    # ------------------
    def test_eval_not_precached_1(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval_not_precached(1, 10)
        self.assertEqual(returned_val, 20)

    def test_eval_not_precached_2(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval_not_precached(704511, 704511)
        self.assertEqual(returned_val, 243)

    def test_eval_not_precached_3(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = collatz_eval_not_precached(81517, 773776)
        self.assertEqual(returned_val, 509)

    # -----
    # print
    # -----
    def test_check_range_1(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = check_range(1, 499)
        self.assertEqual(returned_val, 144)

    def test_check_range_2(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = check_range(501, 999)
        self.assertEqual(returned_val, 179)

    def test_check_range_3(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = check_range(999501, 999999)
        self.assertEqual(returned_val, 290)

    # ----------------
    # one_cycle_length
    # ----------------
    def test_one_cycle_length_1(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = one_cycle_length(1)
        self.assertEqual(returned_val, 1)

    def test_one_cycle_length_2(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = one_cycle_length(837799)
        self.assertEqual(returned_val, 525)

    def test_one_cycle_length_3(self):
        """
        Method will ensure the test is returning the correct collatz value
        :return: will return success or failure based on assertion of equality
        """
        returned_val = one_cycle_length(704511)
        self.assertEqual(returned_val, 243)


    # -----
    # print
    # -----
    def test_print_1(self):
        """
        Method will ensure printing is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        writer = StringIO()
        collatz_print(writer, 1, 10, 20)
        self.assertEqual(writer.getvalue(), "1 10 20\n")

    def test_print_2(self):
        """
        Method will ensure printing is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        writer = StringIO()
        collatz_print(writer, 211817, 633542, 509)
        self.assertEqual(writer.getvalue(), "211817 633542 509\n")

    def test_print_3(self):
        """
        Method will ensure printing is properly done with the given string
        :return: will return success or failure based on assertion of equality
        """
        writer = StringIO()
        collatz_print(writer, 201356, 684930, 509)
        self.assertEqual(writer.getvalue(), "201356 684930 509\n")

    # -----
    # solve
    # -----

    def test_solve_1(self):
        """
        Method will ensure calculation is correct for the given
        simulated file. Given multiple newlines.
        :return: will return success or failure based on assertion of equality
        """
        read = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(),
                         "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2(self):
        """
        Method will ensure calculation is correct for the given
        simulated file. Given multiple newlines.
        :return: will return success or failure based on assertion of equality
        """
        read = StringIO("23545 900418\n993538 566823\n447212 56804\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(),
                         "23545 900418 525\n993538 566823 525\n447212 56804 449\n")

    def test_solve_3(self):
        """
        Method will ensure calculation is correct for the given
        simulated file. Given multiple newlines.
        :return: will return success or failure based on assertion of equality
        """
        read = StringIO("736556 527536\n81843 993308\n880202 469143\n")
        write = StringIO()
        collatz_solve(read, write)
        self.assertEqual(write.getvalue(),
                         "736556 527536 509\n81843 993308 525\n880202 469143 525\n")


# ----
# main
# ----

if __name__ == "__main__":
    main()
