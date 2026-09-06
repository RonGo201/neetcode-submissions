# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    prev_val = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        # left subtree
        if not self.isValidBST(root.left):
            return False
        
        if root.val <= self.prev_val:
            return False
        
        self.prev_val = root.val
        
        # right subtree
        if not self.isValidBST(root.right):
            return False

        return True