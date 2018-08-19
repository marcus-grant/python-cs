from copy import deepcopy
import unittest
import data_structures.heap as heap

class TestHeapModuleFuncs(unittest.TestCase):
    """ Tests the various module scope functions of heap """

    def test_left_child_idx(self):
        """ Test the left_child_idx func """
        givens = [0, 1, 2, 3, 4, 5, 6]
        expect = [1, 3, 5, 7, 9, 11, 13]
        f = lambda x: heap.left_child_idx(x)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)
    
    def test_right_child_idx(self):
        """ Test the right_child_idx func """
        givens = [0, 1, 2, 3, 4, 5, 6]
        expect = [2, 4, 6, 8, 10, 12, 14]
        f = lambda x: heap.right_child_idx(x)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)
    
    def test_parent_idx(self):
        """ Test the parent_idx func """
        givens = [1, 2, 3, 4, 5, 6, 9, 12]
        expect = [0, 0, 1, 1, 2, 2, 4, 5]
        f = lambda x: heap.parent_idx(x)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)

    def test_left_child(self):
        """ Test the left_child func """
        test_heap = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        givens = [0, 1, 2, 3, 4, 5, 6, 12]
        expect = [13, 11, 9, 7, 5, 3, 1, None]
        f = lambda x: heap.left_child(x, test_heap)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)
    
    def test_right_child(self):
        """ Test the right_child func """
        test_heap = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        givens = [0, 1, 2, 3, 4, 5, 6, 12]
        expect = [12, 10, 8, 6, 4, 2, 0, None]
        f = lambda x: heap.right_child(x, test_heap)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)
    
    def test_parent(self):
        """ Test the parent func """
        test_heap = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        givens = [0, 1, 2, 3, 4, 5, 6, 9, 12]
        expect = [None, 14, 14, 13, 13, 12, 12, 10, 9]
        f = lambda x: heap.parent(x, test_heap)
        actual = list(map(lambda x: f(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)
    
    def test_push_max(self):
        """ Test push_max for creating a properly ordered heap """
        givens = [
            (15, [11, 5, 8, 3, 4]),
            (10, []),
            (10, [9]),
            (9, [10]),
            (10, [9, 8]),
            (9, [10, 8]),
            (8, [10, 8, 9]),
            (9, [10, 8, 9, 8]),
            (7, [10, 9, 9, 8, 8]),
        ]
        expect = [
            [15, 5, 11, 3, 4, 8],
            [10],
            [10, 9],
            [10, 9],
            [10, 8, 9],
            [10, 8, 9],
            [10, 8, 9, 8],
            [10, 9, 9, 8, 8],
            [10, 9, 9, 8, 8, 7],
        ]
        f = lambda x: heap.push_max(x[0], x[1])
        actual = deepcopy(givens)
        actual = list(map(lambda x: f(x), actual))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)

    def test_pop_max(self):
        """ Test pop_max for creating a properly ordered heap """
        givens = [
            [11, 5, 8, 3, 4],
            [8, 5, 4, 3],
            [5, 3, 4],
            [4, 3],
            [3],
        ]
        expect = [
            [8, 5, 4, 3],
            [5, 3, 4],
            [4, 3],
            [3],
            []
        ]
        f = lambda x: heap.pop_max(x)
        actual = deepcopy(givens)
        for a in actual:
            _ = f(a)
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)

class TestMaxHeap(unittest.TestCase):
    """ Tests the various functionality of the MaxHeap class """

    def test_init(self):
        """ Test the init func """
        pass