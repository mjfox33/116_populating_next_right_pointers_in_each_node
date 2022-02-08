from dataclasses import dataclass
# Definition for a Node.
@dataclass #this allows me to assert a == b for my testing
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        heap = [root]
        while heap:
            current_node = heap.pop(0)
            if current_node.left and current_node.right:
                current_node.left.next = current_node.right
                if current_node.next:
                    current_node.right.next = current_node.next.left
                heap.append(current_node.left)
                heap.append(current_node.right)
        return root