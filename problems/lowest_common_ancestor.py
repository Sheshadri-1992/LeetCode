# Ref: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findNode(self, node, nodeToMatch, pList):

        if not node:
            return False
        
        if node == nodeToMatch:
           pList.append(node)
           return True

        leftFlag = self.findNode(node.left, nodeToMatch, pList)
        if leftFlag:
           pList.append(node)
           return True
        else:
            rightFlag = self.findNode(node.right, nodeToMatch, pList)
            if rightFlag:
                pList.append(node)
                return True

        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        leftList = []
        rightList = []

        self.findNode(root, p, leftList)
        self.findNode(root, q, rightList)

        leftList.reverse()
        rightList.reverse()

        result = leftList[0]

        for i in range(0, min(len(leftList), len(rightList))):
            if leftList[i] != rightList[i]:
                break

            result = leftList[i]
        
        return result

        
        