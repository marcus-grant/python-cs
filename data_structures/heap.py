from copy import deepcopy

################################
### Heap Traversal Functions ###
################################
def left_child_idx(i):
    """ Performs the arithmetic to get the left child of a given heap index """
    return (i << 1) + 1

def right_child_idx(i):
    """ Performs the arithmetic to get the right child of a given heap index """
    return (i << 1) + 2 

def parent_idx(i):
    """ Performs the arithmetic to get the parent of a given heap index """
    return (i - 1) >> 1

def left_child(i, aheap):
    """ Performs the arithmetic to get the left child of a given heap index """
    index = (i << 1) + 1
    if index >= len(aheap):
        return None
    return aheap[index]
    
def right_child(i, aheap):
    """ Performs the arithmetic to get the right child of a given heap index """
    index = (i << 1) + 2
    if index >= len(aheap):
        return None
    return aheap[index]

def parent(i, aheap):
    """ Performs the arithmetic to get the parent of a given heap index """
    if i == 0:
        return None
    return aheap[(i - 1) >> 1]

def push_max(val, aheap):
    """ Pushes a new value into a heap using the heap ordering rules """
    # Append to end of list backing the heap
    aheap.append(val)

    # Continuously check parent to see if parent is greater,
    # starting from the bottom.
    parent_idx = len(aheap) - 1
    while True:
        # Get next current & parent indices
        current_idx = parent_idx
        parent_idx = (current_idx - 1) >> 1

        # If the parent is smaller than the pushed value, the current index...
        # ... takes the parent value. Otherwise, the current index is the...
        # ... correct position for the pushed value and the process is done.
        p_val = aheap[parent_idx]
        if p_val < val:
            aheap[current_idx] = p_val
        else:
            aheap[current_idx] = val
            return aheap

        # If the process has reached the top of the heap, then it's done
        if parent_idx == 0:
            aheap[parent_idx] = val
            return aheap


def max_heapify(l, i, size):
    """ Takes list 'l' that is not necessarily max heap ordered and
        restores its max heap order. For this to work for every node at i,
        its direct children must violate the heap order, or the process will
        not begin or continue to the children further down the heap.
    """
    # TODO Broken fix plz
    # # Get left/right children indices & heap_len
    # left = (i << 1) + 1
    # right = (i << 1) + 2
    # largest = i

    # # If within heap bounds &
    # # ...left child is larger than current, largest changes to that index
    # if left < size and l[left] > l[largest]:
    #     largest = left
    
    # # If still within heap bounds &
    # # ...right child is larger than new/current largest, change largest to that
    # if right < size and l[right] > l[largest]:
    #     largest = right
    
    # # Untill no child is larger than current root @ i, swap then recurse.
    # if largest != i:
    #     l[i], l[largest] = l[largest], l[i]
    #     max_heapify(l, largest, size)

def build_max_heap(l):
    """ Take any list and in-place re-order it with max heap structure """
    # First the size is needed by max_heapify to check for going out of bounds
    size = len(l)

    # Start from the lowest depth of nodes that has children,
    # ...computed from floor(size/2) - 1 or binary shift right subtract 1,
    # then max heapify the list from that index then decrement that index.
    for i in range((size >> 1) - 1, -1, -1):
        max_heapify(l, i >> 1, size)


def pop_max(aheap):
    """ Pops out & returns the root node & calls max_heapify
        to restore the heap structure """
    size = len(aheap)
    # Edge case for a 1 length heap, just remove the single item
    if size <= 1:
        result = []
        if size == 1:
            result = aheap.pop()
        return result

    # Save the root of the heap to be returned
    root = aheap[0]

    # Then replace the root with the last element & remove last element
    last = aheap.pop()
    aheap[0] = last

    # Max heapify the new root to restore structure.
    max_heapify(aheap, 0, size)

    # Return the old root, which will be the max of the old heap
    return root




# TODO Min heaps
# def min_heapify(l):
#     """ Takes list 'l' and converts to a properly min ordered heap list """
#     return []

# class MaxHeap():
#     def __init__(self, l):
#         """ Initializes the heap, if a list is given, initializes using heapify
#         """
#         self.size = 0
#         self.data = []
#         if type(l) != 'list':
#             raise ValueError("Can only initialize heap with no arguments or a list")
#         else:
#             self.data = deepcopy(l)
#             build_max_heap(self.data)
        
#     def __repr__(self):
#         return '<MaxHeap: {}'.format(self.data)
    
#     # def build(self, l):
#     #     build_max_heap(l)
    
#     # def push(self, x):
#     #     self.data = push_max(x, self.data)
    
#     # def pop()
    
