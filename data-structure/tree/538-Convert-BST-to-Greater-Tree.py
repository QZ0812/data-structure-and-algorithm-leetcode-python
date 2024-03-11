# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n)
# Space Complexity: O(h)
# post order traversal
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumt = 0
        def convertHelper(root):
            nonlocal sumt
            if not root:
                return None

            convertHelper(root.right)
            root.val, sumt = root.val + sumt, sumt + root.val
            convertHelper(root.left)
        convertHelper(root)
        return root
