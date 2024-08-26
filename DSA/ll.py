class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 0  # Instance variable to track the length of the linked list
    
    def append(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
        self.length += 1  # Increment the length when a new node is added
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    def traverse(self):
        curr = self.head
        count = 0  # Local variable to count the nodes during traversal
        while curr:
            count += 1
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        print(f"Length of linked list (calculated during traverse): {count}")
        print(f"Length of linked list (tracked by append method): {self.length}")
        
    def find_middle(self):
        curr = self.head
        size = 0
        while curr:
            size += 1
            curr = curr.next

        curr = self.head
        for i in range(size // 2):
            curr = curr.next

        return curr.val

# Usage
sll = LinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)
sll.append(6)
print(sll.find_middle())  # Output: 1 -> 2 -> 3 -> None
