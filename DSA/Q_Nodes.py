class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue.")
            return None
        item = self.front.val
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        self.size -= 1
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty, nothing to peek.")
            return None
        return self.front.val

    def is_empty(self):
        return self.front is None

    def get_size(self):
        return self.size

# Example usage:
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Front of the queue:", q.peek())
    q.dequeue()
    print("Front of the queue:", q.peek())
    q.dequeue()
    q.dequeue()
    q.dequeue()  # Trying to dequeue from an empty queue
