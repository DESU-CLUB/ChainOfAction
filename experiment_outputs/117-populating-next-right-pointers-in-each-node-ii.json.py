Here's the Python code that follows the given steps to solve the problem:

```python
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root node
        current = root
        
        # Iterate through each level of the tree
        while current:
            dummy = Node(0)  # Dummy node to start the level
            tail = dummy  # Tail to keep track of the last node in the new level
            
            # Iterate through the current level
            while current:
                # Connect the left child if it exists
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                
                # Connect the right child if it exists
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                
                # Move to the next node in the current level
                current = current.next
            
            # Move to the next level
            current = dummy.next
        
        return root
```

This code defines a `Solution` class with a `connect` method that takes the root of a binary tree and connects each node's `next` pointer to its next right node. The method uses a dummy node to keep track of the start of each level and a tail node to connect the children of nodes in the current level. The outer while loop iterates through each level, and the inner while loop connects the nodes within that level. The `current` pointer is used to traverse the nodes at the current level, and it is updated to the first node of the next level at the end of each iteration. The method returns the root of the modified tree.