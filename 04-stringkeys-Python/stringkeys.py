"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
   def __init__(self):
       self.table = ['']*10000
 
   def store(self, string):
    #    """Input a string that's stored in
    #    the table."""
       # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
       # Your code goes here
      
       hv = self.calculate_hash_value(string)
       if(self.table[hv]!= None):
           self.table[hv] = (string)
       else:
           self.table[hv] = [string]
       return hv
      
   def lookup(self, string):
    #    """Return the hash value if the
    #    string is already in the table.
    #    Return -1 otherwise."""
       # Your code goes here
       hv = self.calculate_hash_value(string)
       if(string in self.table[hv]):
           return hv
       return -1
      
 
   def calculate_hash_value(self, string):
    #    """Helper function to calulate a
    #    hash value from a string."""
       # Your code goes here
       hashvalue = ord(string[0])*100 + ord(string[1])
       return hashvalue


