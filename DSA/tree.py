from Q_Nodes import Queue
class TreeNode:
    def __init__(self,value, left=None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root
        
    def breadth_first(self,root):
        output = []
        queu = Queue()
        queu.enqueue(self.root)
        while not queu.is_empty():
            front = queu.dequeue()
            output.append(front.value)
            if front.left:
                queu.enqueue(front.left)
            if front.right:
                queu.enqueue(front.right)
        return output
        
    
    def bfs(self, root, target):
        output = []
        queue = Queue()
        queue.enqueue(self.root)
        path = 1
        while not queue.is_empty():
            path += 1
            front = queue.dequeue()
            output.append(front.value)
            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)
        return path
    def pre_order(self,root):
        output = []
        def _walk(root):
            output.append(root.value)
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
        _walk(root)        
        return output
    
    # def try