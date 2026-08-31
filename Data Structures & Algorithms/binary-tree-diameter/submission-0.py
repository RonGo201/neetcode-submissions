# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0
        diam = self.calc_height(root.left) + self.calc_height(root.right)
        if diam > self.max_diam:
            return diam
        return self.max_diam

    def calc_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h_left, h_right = self.calc_height(root.left), self.calc_height(root.right)
        diam = h_left + h_right
        if diam > self.max_diam:
            self.max_diam = diam
        
        return 1 + max(h_left, h_right)
