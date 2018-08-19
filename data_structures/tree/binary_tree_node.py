from copy import deepcopy

class BinaryTreeNode:
    """ A class representation of binary tree node """
    def __init__(self, left=None, right=None, data=None):
        """ Initializes a binary tree """
        self.left = left
        self.right = right
        self.data = data
    
    def insert(self, val):
        """ Inserts a value (data in Node object) in order """
        if self.data is None:
            self.data = val
            return
        if (val <= self.data):
            if self.left is None:
                self.left = BinaryTreeNode(data=val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BinaryTreeNode(data=val)
            else:
                self.right.insert(val)
    
    def contains(self, val):
        """ Checks a subtree to see if a value is contained inside. """
        if self.data == val:
            return True
        elif val < self.data:
            if self.left is None:
                return False
            else:
                return self.left.contains(val)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(val)
    
    def inorder_traversal(self, f):
        """ Calls a given function, on this node's subtree's
            'data' member in 'inorder' order (ie smallest to largest).
            Args:
                f: a function that gets called on each Node's 'data' member
        """
        if self.left is not None:
            self.left.inorder_traversal(f)
        f(self.data)
        if self.right is not None:
            self.right.inorder_traversal(f)
    
    def inorder_list_recurser(self, l):
        """ Recursively traverses a tree in 'inorder' order so that the
            given list 'l' is ordered from min to max.
        """
        if self.left is not None:
            self.left.inorder_list_recurser(l)
        l.append(self.data)
        if self.right is not None:
            self.right.inorder_list_recurser(l)
    
    def inorder_list(self):
        """ Returns a list of order 'inorder' traversal (ie min->max).
            This function just sets up the recursive calls of --
            -- inorder_list_recurser.
        """
        l = []
        self.inorder_list_recurser(l)
        return deepcopy(l)