from collections import Counter

class Node:
    def __init__(self, value):
        self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
  
    def create_buckets(self):
        return [[] for _ in range(self.size)]
  
    def add(self, key, value):
        """
        # add value into hash map
        # Get the index from the key
        # using hash function
        # Get the bucket corresponding to index
        # check if the bucket has same key as
        # the key to be inserted
        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        # parameters: key, value
        """ 

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))
  
    
    def get(self, key):
        """
        # Return searched value with specific key
        # Get the index from the key using
        # hash function
        # Get the bucket corresponding to index
        # check if the bucket has same key as 
        # the key being searched
        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        # parameters: key
        """ 

        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found"
  
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
  
    def left_join(dict1, dict2):
        return(dict2.update(dict1))
        
    # Driver code
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4}
    
    # This return None
    print(left_join(dict1, dict2))
    
    # changes made in dict2
    print(dict2)