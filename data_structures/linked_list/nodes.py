class LLNode:
    """ A basic (singly) Linked List Node """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def tail(self):
        """ Returns the last LLNode in the list. """
        # If initial sublist location isn't the append location...
        # ... keep updating current location, till no next is found.
        current = self.next
        while current.next is not None:
            current = current.next
        return current
    
    def append(self, data):
        """ Appends arg data to the end of current sublist. """
        # If the given sublist is the last node, then just add to its next
        if self.next is None:
            self.next = LLNode(data=data)
            return

        # Use tail to get the last node to be appended to.
        t = self.tail()
        # Then do the actual appending to the end.
        t.next = LLNode(data=data)
    
    def node_at(self, n):
        """ Gets the nth (zeroth order) node of the list """
        # Handle below range
        if n < 0:
            raise IndexError
        # Handle 0 being a self reference
        elif n == 0:
            return self
        # Handle seeking beyond self if no next is present
        elif self.next is None:
            raise IndexError
        
        # Handle all cases n <= 1 & self.next is not None
        # Start @ i = 1
        current = self.next
        i = 1
        while True:
            # If at the desired index, return the data
            if i == n:
                return current
            
            # Check for going out of bounds of the chain
            if current.next is None:
                raise IndexError
                # return None
            # If not change the current chain link & iterate index
            else:
                current = current.next
                i += 1 # Iterate
    
    def get(self, n):
        """ Gets the nth (zeroth order) element of the list """
        # Just use node_at(n) to get the reference needed to get the value
        return self.node_at(n).data
    
    def insert(self, val, n):
        """ Insert val into nth location (zeroth) order.
            Puts previous node's next reference to this one,
            puts the node at the current position into the next of this one.
        """
        # If at 0, no previous node needs fetch and linking to
        # The given value forms the new start node
        if n == 0:
            # The new next becomes a copy of the current node
            new_next = LLNode(data=self.data, next=self.next)
            # Then self changes its data and next to become the new head
            self.data = val
            self.next = new_next
            return
        # From here on out, all cases are n >= 1

        # Get the node before the desired location that will be needed
        # to link to the newly created node of data = val.
        # node_at handles Index Ranging issues
        prev = self.node_at(n - 1)
        # Get the reference to the next node to be used with the newly inserted
        new_next = prev.next
        new_node = LLNode(data=val, next=new_next)
        prev.next = new_node
    
    def pop(self, n):
        """ Removes the node n jumps from this one and
            links node n - 1 to node n + 1 even if n + 1 is None.
            This removes a value from the list while maintaining list structure
        """
        # Handle removing current node while still maintaining the list refrnse
        if n == 0:
            remove_data = self.data
            if self.next is not None:
                new_self = self.next
                self.data = new_self.data
                self.next = new_self.next
            else:
                self.data = None
            return remove_data
        
        prev = self.node_at(n - 1)
        remove = prev.next
        new_next = remove.next
        prev.next = new_next
        return remove.data
        
