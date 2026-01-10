# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        zigZagLevelOrder = []
        myQueue = collections.deque()

        myQueue.append(root)
        depth = 0 # when depth%2 is 0, right to left; when depth%2 is 1, left to right

        while myQueue:

            level = []
            while len(myQueue) > 0:
                ele = myQueue.popleft()
                if ele:
                    level.append(ele)

            levelList = []
            # print(level)
            if len(level) > 0:
                for element in level:
                    if element:
                        if element.left:
                            myQueue.append(element.left)
                        if element.right:
                            myQueue.append(element.right)

                        levelList.append(element.val)
            
            if depth%2 == 1:
                levelList.reverse()
            
            if len(levelList) > 0:
                zigZagLevelOrder.append(levelList)
            
            depth = depth + 1

        
        return zigZagLevelOrder