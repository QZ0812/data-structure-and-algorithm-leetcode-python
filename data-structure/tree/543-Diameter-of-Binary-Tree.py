# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n) -- n is the number of tree nodes
# Space Complexity: O(h)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = 0
        
        def max_Depth(root):
            nonlocal max_diameter
            
            if not root:
                return 0

            l = max_Depth(root.left)
            r = max_Depth(root.right)

            max_diameter = max(l + r, max_diameter)

            return 1 + max(l , r)
      
        max_Depth(root)
        return max_diameter
