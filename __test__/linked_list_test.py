import unittest

import data_structures.linked_list.nodes
import data_structures.linked_list.llist

LLNode = data_structures.linked_list.nodes.LLNode
LList = data_structures.linked_list.llist.LList

class TestLLNode(unittest.TestCase):
    """ Test the LLNode class (singly linked) """

    def test_append_and_get_correctness(self):
        """ Tests the functionality of appending and getting values """
        givens = [ # (append values, get idxs)
            ([0], [0]),
            ([1, 2, 3, 4], [3, 2, 1, 0]),
        ]
        expects = [
            [0],
            [4, 3, 2, 1],
        ]
        actuals = []
        for g in givens:
            appends = g[0]
            gets = g[1]
            current_results = []
            ll = None
            for ap in appends:
                if ll is None:
                    ll = LLNode(data=ap)
                else:
                    ll.append(ap)
            for ge in gets:
                current_results.append(ll.get(ge))
            actuals.append(current_results)
        for g, e, a in zip(givens, expects, actuals):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)
    
    def test_get_index_error(self):
        """ Test that IndexError is raised if getting too low
            or high an index. """
        ll = LLNode(data=0)
        with self.assertRaises(IndexError):
            ll.get(-100)
        with self.assertRaises(IndexError):
            ll.get(100)
        ll.append(1)
        ll.append(2)
        with self.assertRaises(IndexError):
            ll.get(-100)
        with self.assertRaises(IndexError):
            ll.get(100)
    
    def test_insert_correctness(self):
        """ Test that insert() works correctly 
            by inserting an 'x' into several indices """
        givens = [ # (append values, insert values)
            ([0], [0]), # insert @ head of len len 1 list
            ([0], [1]), # insert @ end of len 1 list
            ([0, 1], [0]), # insert @ head of len > 1 list
            ([0, 1], [1]), # insert before end of list after head
            ([0, 1], [2]), # insert @ end of list of len > 1
            ([0, 1, 2], [2]) # insert @ middle of list with item next
        ]
        expects = [
            ['x', 0],
            [0, 'x'],
            ['x', 0, 1],
            [0, 'x', 1],
            [0, 1, 'x'],
            [0, 1, 'x', 2],
        ]
        actuals = []
        for g in givens:
            appends = g[0]
            inserts = g[1]
            current_results = []
            ll = None
            for ap in appends:
                if ll is None:
                    ll = LLNode(data=ap)
                else:
                    ll.append(ap)
            for ins in inserts:
                ll.insert('x', ins)
            for i in range(len(g[0]) + 1):
                current_results.append(ll.get(i))
            actuals.append(current_results)
        for g, e, a in zip(givens, expects, actuals):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)
        
    def test_pop_correctness(self):
        """ Test that pop(n) works correctly 
            by removing values at different positions of same list """
        input_list = LLNode(data=0)
        for i in range(1, 5):
            input_list.append(i)
        givens = [2, 3, 1, 0]
        expects = [
            [0, 1, 3, 4],
            [0, 1, 3],
            [0, 3],
            [3],
        ]
        actuals = []
        length = 4
        for pop_idx in givens:
            current_results = []
            _ = input_list.pop(pop_idx)
            i = 0
            while i < length:
                current_results.append(input_list.get(i))
                i += 1
            length -= 1
            actuals.append(current_results)
        for g, e, a in zip(givens, expects, actuals):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)
        

class TestLList(unittest.TestCase):
    """ Test the LList class """

    def test_append_with_len_head_tail(self):
        """ Tests the append function against member vars _len, _head, _tail"""
        pass