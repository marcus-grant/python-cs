import unittest
import random
# import os
# import sys

from algorithms.sort.bubble_sort import bubble_sort

random.seed(42)

class TestBubbleSortModule(unittest.TestCase):
    """ Test class for the whole Bubble Sort module """

    def test_bubble_sort_correctness(self):
        given = [
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 1, 7, 6, 5, 4, 3, 2, 8, 0],
            [random.randrange(1, 11, 1) for _ in range(100)],
            [random.randrange(1, 101, 1) for _ in range(100)],
            [random.randrange(1, 1001, 1) for _ in range(1000)],
        ]
        for g in given:
            expect = g.copy()
            expect.sort()
            actual = g.copy()
            bubble_sort(actual)
            msg = "Given:\n{}\nExpected:\n{}\nActual:\n{}\n"
            msg = msg.format(g, expect, actual)
            self.assertListEqual(expect, actual, msg=msg)