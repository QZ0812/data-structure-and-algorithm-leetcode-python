# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        lenth, stack = len(nums), []
        ans = [-1]*lenth

        nums = nums + nums
        for i, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                index, val = stack.pop()
                if index < lenth:
                    ans[index] = num
            stack.append((i, num))
        return ans
