class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0  # Instance variable to track the length of the linked list

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * self.__size
        self.keys = []
        
    def __hash(self, key):
        return sum([ord(char) for char in key]) * 255 % self.__size
    
    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            ll = LinkedList()
            self.__buckets[index] = ll
        self.__buckets[index].insert((key, value))
        self.keys.append(key)
    def get(self, key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is None:
            return None
        curr = bucket.head
        while curr:
            if curr.val[0] == key:
                return curr.val[1]
            curr = curr.next
    
    def has (self, key):
        if self.get(self, key) is not None:
            return True
        return False
    
    def keys(self):
        """
        Returns a list of all keys stored in the hash table.
        """
        return self.keys
             
        