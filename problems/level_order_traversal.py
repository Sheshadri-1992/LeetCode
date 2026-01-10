# Definition for a binary tree node.
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levelOrderList = []

        myQueue = collections.deque()
        myQueue.append(root)

        while myQueue:
            level = []

            # pop all the elements in this level
            while len(myQueue)>0:
                element = myQueue.popleft()
                if (element):
                    level.append(element)

            for element in level:
                if element:
                    if element.left:
                        myQueue.append(element.left)
                    if element.right:
                        myQueue.append(element.right)

            if len(level) > 0:
                levelList = []
                for element in level:
                    levelList.append(element.val)
                    
                if len(levelList)>0:
                    levelOrderList.append(levelList)

        return levelOrderList





