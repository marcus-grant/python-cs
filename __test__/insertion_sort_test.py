from copy import deepcopy
import unittest
import random

random.seed(42)

import algorithms.sort.insertion_sort as ins

class TestInsertionSort(unittest.TestCase):
    """ Test the insertion sort function """

    def test_insertion_sort(self):
        """ Test the insertion sort function for various cases.
            Should match the results of Python's sort func.
        """
        given = [
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [4, 1, 2, 1, 2, 4, 1, 2, 1, 4, 1],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [random.randrange(0, 10) for _ in range(10)],
            [random.randrange(0, 10) for _ in range(1000)],
            [random.randrange(0, 1000) for _ in range(1000)],
            # [random.randrange(0, 100) for _ in range(10**5)],
            # [random.randrange(0, 10**5) for _ in range(10**5)],
        ]
        actual = deepcopy(given)
        for a in actual:
            ins.insertion_sort(a)
        expect = deepcopy(given)
        for e in expect:
            e.sort()
        for g, e, a in zip(given, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)
            # self.assertListEqual(e, a)