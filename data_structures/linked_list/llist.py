from . import nodes
LLNode = nodes.LLNode

class LList:
    """ Linked List class that mostly just is an interface to LLNode """
    
    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None
    