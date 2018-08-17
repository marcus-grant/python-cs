import unittest
import random

random.seed(42)

import algorithms.sort.merge_sort as ms

class TestMergeSort(unittest.TestCase):
    """ Test the merge sort function """

    def test_merge_sort(self):
        """ Test the merge sort function for various cases.
            Should match the results of Python's sort func.
        """

        given = [
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [4, 1, 2, 1, 2, 4, 1, 2, 1, 4],
            [random.randrange(0, 10) for _ in range(10)],
            [random.randrange(0, 10) for _ in range(1000)],
            [random.randrange(0, 1000) for _ in range(1000)],
            [random.randrange(0, 100) for _ in range(10**5)],
            [random.randrange(0, 10**5) for _ in range(10**5)],
        ]
        actual = given.copy()
        for a in actual:
            ms.merge_sort(a)
        expect = given.copy()
        for e in expect:
            e.sort()
        for g, e, a in zip(given, expect, actual):
            msg = "given:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)
            # self.assertListEqual(e, a)