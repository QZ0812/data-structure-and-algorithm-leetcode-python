# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root, is_left, total):
            if not root: 
                return total
            if is_left and not root.left and not root.right:
                return total + root.val
            
            return helper(root.left, True, total) + helper(root.right, False, total)
             
        return helper(root, False, 0)
