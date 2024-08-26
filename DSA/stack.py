class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class Stack:
    def __init__(self, top=None):
        self.top = top
        self.size = 0

    def push(self, val):
        if self.top:
            node = Node(val)
            node.next = self.top
            self.top = node
        else:
            self.top = Node(val)
        self.size += 1
            