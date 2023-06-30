"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        realhashnumber = self.calculate_hash_value(string)
        self.table[realhashnumber] = string
        pass

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        realhashnumber = self.calculate_hash_value(string)
        if (self.table[realhashnumber] is not None):
            return realhashnumber
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if len(string) < 2:
            return None
        temphashnumber = ord(string[0])
        temphashnumber2 = ord(string[1])
        realhashnumber = temphashnumber * 100 + temphashnumber2
        return realhashnumber
    

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
