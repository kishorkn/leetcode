# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []  # Return an empty list if the tree is empty

        result = []
        queue = deque([root])  # Initialize a queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            level = []  # List to store the current level's values

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue the front node
                level.append(node.val)  # Add the node's value to the level list

                # Enqueue the left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # Append the current level to the result

        return result

if __name__ == "__main__":
    # Helper function to create a binary tree from a list of values
    def create_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    # Test case 1
    values1 = [3, 9, 20, None, None, 15, 7]
    root1 = create_tree(values1)
    sol = Solution()
    print(sol.levelOrder(root1))  # Output: [[3, 9, 20], [15, 7]]

    # Test case 2
    values2 = [1, 2, 3, 4, 5]
    root2 = create_tree(values2)
    print(sol.levelOrder(root2))  # Output: [[1], [2, 3], [4, 5]]