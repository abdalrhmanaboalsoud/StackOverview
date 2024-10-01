class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackNodes:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def get_size(self):
        return self.size

# Example usage:
if __name__ == "__main__":
    s = StackNodes()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top of the stack:", s.peek())
    s.pop()
    print("Top of the stack:", s.peek())
    s.pop()
    s.pop()
    s.pop()  # Trying to pop from an empty stack
