import unittest

from data_structures.tree import binary_tree_node
Node = binary_tree_node.BinaryTreeNode

# Aliases
Node = binary_tree_node.BinaryTreeNode

class TestBinaryTreeNode(unittest.TestCase):
    """ Tests the binary_tree_node module """

    def test_insert_and_inorder_list(self):
        givens = [
            [3, 1, 2, 0, 5, 4, 6],
        ]
        expects = [
            [0, 1, 2, 3, 4, 5, 6],
        ]
        actuals = []
        node_tree = None
        for g in givens:
            node_tree = Node()
            for x in g:
                node_tree.insert(x)
            actuals.append(node_tree.inorder_list())
            node_tree = None
        for g, e, a in zip(givens, expects, actuals):
            msg = "\n\ngiven:\n{}\nexpected:\n{}\nactual:\n{}\n"
            msg = msg.format(g, e, a)
            self.assertListEqual(e, a, msg=msg)

        