# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # for max depth, lets use a BFS traversal to find out the levels
        dq=deque()
        dq.append(root)
        depth=0

       
        while dq:
            # for the current leve
            for i in range(len(dq)):
                node=dq.popleft()

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth+=1
        return depth

                

      


        
        