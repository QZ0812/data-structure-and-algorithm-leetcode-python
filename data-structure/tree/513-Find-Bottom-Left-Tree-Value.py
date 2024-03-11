# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# BFS solution
# Time Complexity: O(n)
# Space Complexity: O(n)   
from collections import deque 
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right: q.append(node.right)
            if node.left: q.append(node.left)
                
        return node.val


#DFS solution
# Time Complexity: O(n)
# Space Complexity: O(h)  
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        result, h = self.dfs(root, 0, root.val, 0)
        return result
    
    def dfs(self, root, h, result, h_max):
        
        if not root:
            return result, h_max
        
        if not root.left and not root.right:
            if h > h_max:
                return root.val, h
        
        result, h_max = self.dfs(root.left, h+1, result, h_max)
        result, h_max = self.dfs(root.right, h+1, result, h_max)
        return result, h_max
