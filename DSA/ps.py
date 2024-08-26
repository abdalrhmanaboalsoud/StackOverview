# Problem 1: Implement a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Problem 2: Reverse a Linked List
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev


# Problem 3: Find the Middle of a Linked List
def find_middle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data if slow else None


# Problem 4: Detect a Cycle in a Linked List
def detect_cycle(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Problem 5: Merge Two Sorted Linked Lists
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next


# Problem 6: Remove Duplicates from a Sorted Linked List
def remove_duplicates(linked_list):
    current = linked_list.head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next


# Problem 7: Implement a Stack Using Linked List
class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return self.head is None


# Problem 8: Balanced Parentheses
def balanced_parentheses(expr):
    stack = Stack()
    for char in expr:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if not ((char == ")" and top_char == "(") or
                    (char == "}" and top_char == "{") or
                    (char == "]" and top_char == "[")):
                return False
    return stack.is_empty()


# Problem 9: Evaluate Postfix Expression
def evaluate_postfix(expr):
    stack = []
    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
            if char == "+":
                stack.append(val1 + val2)
            elif char == "-":
                stack.append(val1 - val2)
            elif char == "*":
                stack.append(val1 * val2)
            elif char == "/":
                stack.append(val1 // val2)
    return stack.pop()


# Problem 10: Sort a Stack
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


# Problem 11: Next Greater Element
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result


# Problem 12: Implement a Queue Using Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        if not self.front:
            return None
        dequeued = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued

    def peek(self):
        return self.front.data if self.front else None

    def is_empty(self):
        return self.front is None


# Problem 13: Implement a Circular Queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None
        dequeued = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return dequeued


# Problem 14: Reverse a Queue
def reverse_queue(queue):
    if queue.is_empty():
        return
    data = queue.dequeue()
    reverse_queue(queue)
    queue.enqueue(data)


# Problem 15: Generate Binary Numbers Using a Queue
def generate_binary_numbers(n):
    queue = Queue()
    queue.enqueue("1")
    result = []
    for i in range(n):
        front = queue.dequeue()
        result.append(front)
        queue.enqueue(front + "0")
        queue.enqueue(front + "1")
    return result


# Problem 16: Interleave the First Half of a Queue with the Second Half
def interleave_queue(queue):
    stack = Stack()
    half_size = queue.size() // 2

    for _ in range(half_size):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    for _ in range(half_size):
        queue.enqueue(queue.dequeue())

    for _ in range(half_size):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())
        queue.enqueue(queue.dequeue())


# Problem 17: Implement a Stack Using Two Queues
class StackUsingQueues:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):
        if self.q1.is_empty():
            return None
        while self.q1.front != self.q1.rear:
            self.q2.enqueue(self.q1.dequeue())
        popped = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return popped


# Problem 18: Implement a Queue Using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()


# Problem 19: Palindrome Checker Using Stack and Queue
def palindrome_checker(s):
    stack = Stack()
    queue = Queue()
    for char in s:
        stack.push(char)
        queue.enqueue(char)

    while not stack.is_empty():
        if stack.pop() != queue.dequeue():
            return False
    return True


# Test cases for demonstration
if __name__ == "__main__":
    # Linked List Operations
    ll = SinglyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.traverse()
    
    reverse_linked_list(ll)
    ll.traverse()

    print(f"Middle of the Linked List: {find_middle(ll)}")

    # Stack Operations
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Popped: {stack.pop()}")
    print(f"Peek: {stack.peek()}")

    # Queue Operations
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Peek: {queue.peek()}")

    # Other problems can be tested similarly by creating instances and invoking methods.
