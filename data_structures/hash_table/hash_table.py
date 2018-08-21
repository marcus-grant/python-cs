""" Implementation of a hash table using linear probing in collision resolution
"""

# TODO: Refactor so a new func idx_and_val_from_key(key) can be reused for:
#   - _put
#   - _get
#   - __contains__
#   - __delitem__
#   This is helpful because:
#   1. Reuse of a lot of the same code involved in linear probing during access
#   2. More options for raising or not raising errors for KeyError
#   3. Readibility

# TODO: try using linked lists
# A great diagram that pretty much explains all:
#   https://en.wikipedia.org/wiki/Hash_table

# TODO: This really needs __contains__ which means redoing _get --
#      __get shouldn't raise anything instead return None if not found.
#       Then the getitem & setitem handles the raising of keyerror

from copy import deepcopy
class HashTable:
    """ A hash table object that performs hash table functions
        using only lists, hash functions, & linked lists.
    """

    # Grow & Shrink ratios to be used to determine when the table --
    # --needs to grow or shrink in size. Tweak as needed.
    # I tend to lean on optimizing for computation time over --
    # memory usage so I'll use a somewhat low load-factor
    # More often than not, I've had to optimize systems due to --
    # them taking too much CPU time over them taking too much RAM.
    ratio_expand = 0.66
    ratio_shrink = 0.2
    min_size = 11

    def __init__(self, size=None):
        self._size = size if size is not None else self.min_size
        self._records = [(None, None)] * self._size
        self._count = 0
        # Tracks when/where hash collisions occur
        self._latest_conflicting_idx = None
    
    ################################
    ## Internal Mechanical Methods #
    ################################
    # def _hashed_index_from_key(key, size=self._size):
    #     """ The main function of this hash table. Gets used for almost every
    #         operation of a hash table.
    #         This takes a key, and a size to modulo against, and produces
    #         an index from their hash result.
    #         If a collision occurs, that initial index is stored in
    #         self._latest_conflicting_index so linear probing functions properly
            # """
    def _put(self, key, val):
        """ Sets the value @ key to val, or creates a new one with key
            if nothing is already there.
        """
        # Get the hash value
        H = hash(key)

        # Convert the hash to an index for the current _keys
        idx = H % self._size

        # Check if the current slot is occupied and has the given key
        # This indicates the table already has this key/val allocated.
        # Now it simply needs its value changed.
        if self._keys[idx] == key:
            self._values[idx] = val
            return
        
        # Now we know a new location with associated index needs to be --
        # either allocated or rehashed due to a key collision.
        # First check if the slot is empty
        if self._keys[idx] is None:
            # If empty set flag to False so collision handling is skipped
            key_occupied = False
            # Set the new value, and update the count variable
            self._keys[idx] = key
            self._values[idx] = val
            self._count += 1
            # Now that the count has been updated, the table may need to --
            # grow or shrink according to the fill ratio
            self._update_capacity()
            return
        
        # Since the key is occupied either this key has already been --
        # allocated, but was rehashed to get there and needs to be found. 
        # Or the key needs to find an open slot to be rehashed.
        # Start by creating some event flags.
        # Since we're here the key location is definitely occupied
        key_occupied = True
        # This flag corresponds to the event of the key being found.
        key_found = False
        # Keep rehashing until no collision occurs
        while key_occupied and (not key_found):
            print("rehashing")
            # Rehash with simple linear probing
            idx = (idx + 1) % self._size
            # Check if key is occupied & update the flag for that event
            if self._keys[idx] is None:
                key_occupied = False
            elif self._keys[idx] == key:
                key_found = True

        # Now an index for _keys should be found that is either --
        # not occupied or corresponds to a rehashed location for --
        # the current key.
        # Now check if the key was found.
        if key_found:
            # Replace the existing value in this location
            self._values[idx] = val
        # If the key wasn't found, then put the key/value --
        # in this new rehashed location that is empty
        else:
            self._keys[idx] = key
            self._values[idx] = val
            # Now update the count and update according to fill ratio
            self._count += 1
            self._update_capacity()
            
    def _get(self, key):
        """ Returns the reference tied to a key """
        # TODO: Grow/Shrink
        # The basic functionality is this:
        # H = hash(key)
        # N = len(buckets)
        # value @ key = buckets[H % N]
        # Get the hash from the key
        # Convert the hash to an index for the current buckets list
        idx = hash(key) % self._size

        # Check if they key was found during first hash
        if self._keys[idx] == key:
            # Simply return the value if so
            return self._values[idx]
        
        # Some event flags will be helpful here.
        no_loop = True # Check if a loop has occurred while rehashing
        key_not_found = True # Check if key was found
        occupied = True # Check if location is empty

        # To detect a loop we need the initially hashed index
        first_idx = idx

        while key_not_found and occupied and no_loop:
            # Rehash the index
            idx = hash(key + 1) % self._size
            # Check if key was found
            if self._keys[idx] == key:
                key_not_found = False
            # Check if key is unoccupied
            elif self._keys[idx] is None:
                occupied = False
            # Check first hash was reached, indicating that the key --
            # definitely hashn't been placed in this table.
            elif first_idx == idx:
                no_loop = False
        
        # Now handle each event accordingly.
        # Starting with the key being found
        if not key_not_found:
            # Return the value at the rehashed position
            return self._values[idx]
        # If this step in the function is reached it means --
        # the key was never assigned a value in the table.
        # This should result in a KeyError
        raise KeyError

    def _reallocate(self):
        """ Gets called when size of table changes to reallocate keys & values
        """
        # TODO: There might be a more space efficient way to reassign all keys
        # Rebuild the keys list
        # Start by creating a copy of this hash table to maintain old keys/vals
        old_table = deepcopy(self)

        # Go through every currently assigned key.
        # Use put(key) to access the old value associated with it.
        # Put the current key and its associated value in their new lists.
        for key in old_table._keys:
            if key is None: # if slot is empty skip
                continue
            # get the value associated with current key
            val = old_table._get(key)
            # put it into this newly allocated table
            # When this is done the new table should be recovered in new size
            self._put(key, val)
            
    
    def _update_capacity(self):
        """ Checks the current number of entries (length) to determine if --
            -- the capacity should be increased, decreased, or nothing to do.
            If the size is changed then the buckets & entries are reallocated.
        """
        fill_ratio = self._count / self._size

        # Determine if growth, shrinking, or nothing needs to be done
        # Growing and shrinking is doubling + 1 and -1 + halving
        # This is to have more prime numbered bucket sizes which works out
        # to have better hashing properties due to how modulos work
        if fill_ratio > self.ratio_expand:
            # Set the capacity to increase by doubling and adding 1
            self._size = (self._size << 1) + 1
        elif fill_ratio < self.ratio_shrink and self._size > self.min_size:
            # Set the capacity to shrink by halfing
            self._size = (self._size - 1) >> 1
        else:
            # If fill ratio is between the growth & shrink ratios, do nothing
            return
        
        # With a new size, the table needs to be reallocated with all key/vals
        self._reallocate()
    
    # TODO: !!!! Really inefficient recode with shared member func for access
    def _remove(self, key):
        """ Removes key and its associated value from this table.
            It then calls update_capacity to check if resize/reallocate needed
        """
        # Remember this is inefficient but I want something running now
        # Since I don't want to rewrite the accessing algorithm again...
        # ...scan the key list to get the index to remove key and val from
        idx = 0
        last_idx = len(self._keys) - 1
        idx_found = False
        while idx <= last_idx:
            if key == self._keys[idx]:
                idx_found = True
                break
        
        # If the key wasn't found, raise KeyError
        if not idx_found:
            raise KeyError
        
        # Now blank out the key & val from their lists
        self._keys[idx] = None
        self._values[idx] = None
        # Then update the count member variable
        self._count -= 1
        # Then finally update capacity with new fill ratio
        self._update_capacity()


    ################################
    ### Builtin Method Overrides ###
    ################################
    def __setitem__(self, key, value):
        """ Implements built in object[key] = value setting functionality """
        # Simply use the put method
        self._put(key, value)

    def __getitem__(self, key):
        """ Implements the built in object[key] access functionality """
        # Simply use the get method
        return self._get(key)
    
    def __delitem__(self, key):
        """ Handles the builtin deletion """
        # Simply use _remove
        self._remove(key)
    
    def __len__(self):
        return self._count
    
    def __iter__(self):
        for key in self._keys:
            if key is not None:
                yield self._get(key)
    