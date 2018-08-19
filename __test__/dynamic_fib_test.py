import unittest
import algorithms.dynamic_programming.dynamic_fib as fib

class TestDynamicFib(unittest.TestCase):
    """ Tests the dynamic fibonacci module """
    def test_dynamic_fib(self):
        """ Test dynamic fib func for correctness """
        givens = [x for x in range(-1, 21, 1)] # [-1, 0, 1, 2, ..., 20]
        expect = [0, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
            144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
        actual = list(map(lambda x: fib.fibonacci(x), givens))
        for g, e, a in zip(givens, expect, actual):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertEqual(e, a, msg=msg)