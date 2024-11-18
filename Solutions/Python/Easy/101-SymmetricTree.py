"""
    101 Symmetric Tree
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is symmetric around its center.

        This function determines whether the given binary tree is a mirror of itself,
        i.e., symmetric around its center.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """
        if not root:
            return True  # An empty tree is symmetric

        def isMirror(t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
            """
            Helper function to check symmetry between two subtrees.

            Args:
                t1 (Optional[TreeNode]): The root of the first subtree.
                t2 (Optional[TreeNode]): The root of the second subtree.

            Returns:
                bool: True if the subtrees are mirrors of each other, False otherwise.
            """
            if not t1 and not t2:
                return True  # Both subtrees are empty
            if not t1 or not t2:
                return False  # One subtree is empty, the other is not
            # Check if the current nodes are the same and their subtrees are mirrors
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))

        # Check symmetry between left and right subtrees of the root
        return isMirror(root.left, root.right)
    
if __name__ == "__main__":
    # Example usage
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    solution = Solution()
    result = solution.isSymmetric(root)
    print(f"Is the tree symmetric? {result}")