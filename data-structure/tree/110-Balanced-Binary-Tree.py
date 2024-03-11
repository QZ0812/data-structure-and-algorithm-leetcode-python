# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#similar as leetcode 104, but addition step is to check left max and right max height difference. 
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return not self.maxDepth(root) == -1
        
    
    def maxDepth(self, root):
        if not root:
            return 0
        
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        
        if (abs(l - r) > 1 or l == -1 or r == -1):
            return -1
        
        return 1 + max(l, r)
