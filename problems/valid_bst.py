# Ref: https://leetcode.com/problems/validate-binary-search-tree/submissions/1881472857/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, root, leftVal, rightVal):

        if root == None:
            return True

        # This is the most important condition
        if leftVal < root.val < rightVal:
            pass
        else:
            return False

        # the nodes in the left sub tree is bounded to the right by current node value, and the minimum value passed along
        # i.e it enusres the constraint of the subsequent values should be bounded within the root.val
        leftFlag = self.isValid(root.left, leftVal, root.val)

        # the nodes in the right sub tree is bounded to the left by current node value, and the maximum value passed along
        # i.e it enusres the constraint of the subsequent values should be always more than the root.val
        rightFlag = self.isValid(root.right, root.val, rightVal)

        return leftFlag and rightFlag

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True

        if root.left == None and root.right == None:
            return True
        
        result = self.isValid(root, float("-inf"), float("inf"))
        return result