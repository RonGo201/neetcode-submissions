# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        self.height(root)
        return self.isBalanced

    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        h_left, h_right = self.height(root.left), self.height(root.right)
        if (h_left - h_right) > 1 or (h_left - h_right) < -1:
            self.isBalanced = False

        return 1 + max(self.height(root.left), self.height(root.right))