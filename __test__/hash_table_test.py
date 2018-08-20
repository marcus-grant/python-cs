import unittest
import random
import string

random.seed(42)

import data_structures.hash_table.hash_table

HashTable = data_structures.hash_table.hash_table.HashTable

min_char = 4
max_char = 16

all_chars = string.ascii_letters + string.punctuation + string.digits

def rand_str():
    s = ''
    for _ in range(random.randint(min_char, max_char)):
        s += random.choice(all_chars)
    return s

class TestHashTable(unittest.TestCase):
    """ Tests the HashTable Class """

    # TODO: Add more mocking vals like objects, lists, funcs, tuples, etc.
    def test_access(self):
        """ Test the getitem/setitem builtin override, which also tests
            the important workhosrse method _entry_from_key(key)
        """

        size = 60
        num_keys = [random.randint(0, 10**6) for _ in range(size >> 1)]
        str_keys = [rand_str() for _ in range(size - len(num_keys))]
        keys =  num_keys + str_keys
        keys = num_keys
        num_vals = [random.uniform(-1000, 1000) for _ in range(size >> 1)]
        str_vals = [rand_str() for _ in range(size - len(num_vals))]
        vals = str_vals + num_vals
        vals = num_vals
        h = HashTable()
        for i in range(len(keys)):
            key = keys[i]
            h[key] = vals[i]
        self.assertEqual('blah', h['a'])
