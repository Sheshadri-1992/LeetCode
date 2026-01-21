# Definition for a binary tree node.
# Ref: https://leetcode.com/problems/diameter-of-binary-tree/description/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    diameter = 0

    def heightOfTree(self, root):

        if not root:
            return 0

        # if root and root.left == None and root.right == None:
        #     return 0
        
        leftTree = self.heightOfTree(root.left)
        rightTree = self.heightOfTree(root.right)

        self.diameter = max(self.diameter, leftTree + rightTree)

        return 1+max(leftTree, rightTree)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root and root.left == None and root.right == None:
            return 0

        treeHeight = self.heightOfTree(root)
        return self.diameter

        