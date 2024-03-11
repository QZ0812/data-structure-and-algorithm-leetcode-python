# high voted anwser in leetcode: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        ans = self.find_path_sum_with_root(root, targetSum, 0)
        ans += self.pathSum(root.left, targetSum) 
        ans += self.pathSum(root.right, targetSum) 
                
        return ans
    
                
    def find_path_sum_with_root(self, root, targetSum, count):

        if not root:
            return count

        if targetSum == root.val:
            count += 1

        count = self.find_path_sum_with_root(root.left, targetSum - root.val, count)
        count = self.find_path_sum_with_root(root.right, targetSum - root.val, count)

        return count
