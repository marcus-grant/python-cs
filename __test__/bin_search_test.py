import unittest

from algorithms.search.binary_search import binary_search_nearest

class TestBinarySearchNearest(unittest.TestCase):
    """ Test the binary_search_nearest func """

    def test_binary_search_nearest(self):
        """ Tests the binary search nearest func for correctness """
        big_list = [x for x in range(10**6)]
        given_lists = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], # 2
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], # 4
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], # 6
            big_list,
        ]
        given_search_vals = [
            0.2,
            2.7, # 2
            4.3,
            7.1, # 4
            8.9,
            7,   # 6
            10**6 - 2,
        ]
        expect = [
            0,
            3, # 2
            4,
            7, # 4
            9,
            7, # 6
            10**6 - 2,
        ]
        actuals = []
        for ls, sr in zip(given_lists, given_search_vals):
            idx = binary_search_nearest(ls, sr)
            actuals.append(idx)
        test_zip = zip(given_lists, given_search_vals, expect, actuals)
        for gl, gs, e, a in test_zip:
            msg = "\n\ngivens: search = {} in...\n{}"
            msg += "\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(gs, gl, e, a)
            self.assertEqual(e, a, msg=msg)