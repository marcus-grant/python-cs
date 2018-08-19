from . import binary_tree_node
Node = binary_tree_node.BinaryTreeNode

# TODO: Give selector member variable that selects between--
# -- array or linked list backing.
class BinaryTree():
    """ A complete binary tree, with binary search & tree functions """
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, val):
        """ Inserts a value (data in Node object) in order """
        if self.root is None:
            self.root = Node(data=val)
            return
        self.root.insert(val)
    
    def inorder_values(self, val):
        """ Walk through the tree and return a list of values 'inorder' """ 
        if self.root is None:
            return []
        