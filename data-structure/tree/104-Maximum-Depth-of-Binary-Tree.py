# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursion 
# Time Complexity: O(n)
# Space Complexity: O(h)
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
     
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# iterative
# Time Complexity: O(n)
# Space Complexity: ~~O(1)
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        q = deque([root])

        height = 0
        
        while q:
            
            height += 1
            q_lenth = len(q)
            
            while q_lenth:
                root = q.popleft()
                
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                    
                q_lenth -= 1
                
        return height
