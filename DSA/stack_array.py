class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop.")
            return None
        item = self.stack.pop()
        print(f"Popped: {item}")
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek.")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage:
if __name__ == "__main__":
    s = StackArray()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top of the stack:", s.peek())
    s.pop()
    print("Top of the stack:", s.peek())
    s.pop()
    s.pop()
    s.pop()  # Trying to pop from an empty stack
