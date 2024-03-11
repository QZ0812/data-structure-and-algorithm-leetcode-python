

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# in order traversal
# Time Complexity: O(lgn)
# Space Complexity: O(h) 
from collections import deque

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mins,  previous = float('inf'), float('inf')
        
        def dfs(root):
            nonlocal mins, previous
            if not root:
                return
            
            dfs(root.left)
            mins = min(mins, abs(previous - root.val))
            previous = root.val
            dfs(root.right)

            return
  
        dfs(root)
        return mins
