from collections import deque
class TreeNode:
    def __init__(self,value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, node):
        self.queue.append(node)

    def dequeue(self):
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def bfs(self, root, target):
        output = []
        queue = Queue()
        queue.enqueue(self.root)
        edges = 0  # Start counting edges
        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)
            if front.left:
                queue.enqueue(front.left)
                edges += 1  # Count the edge to the left child
            if front.right:
                queue.enqueue(front.right)
                edges += 1  # Count the edge to the right child
        return edges  # Return the count of edges

# Example usage:
if __name__ == "__main__":
    # Creating a binary tree
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(13)
    tree.insert(18)

    # Counting the edges
    edges_count = tree.bfs(tree.root, None)
    print("Number of edges:", edges_count)
