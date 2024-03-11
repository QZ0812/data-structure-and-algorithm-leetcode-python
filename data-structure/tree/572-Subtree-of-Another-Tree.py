# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

# Time Complexity: O(n * m) -- n is the number of nodes in the root tree. m is the number of nodes in the subRoot tree.
# Space Complexity: O(h) -- h is the height of the call stack during the recursive traversal.
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if not root:
            return False
        
        if not subRoot:
            return True
        
        if self.sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
               
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if not root:
            return False
        
        if not subRoot:
            return False
        
        if root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False
