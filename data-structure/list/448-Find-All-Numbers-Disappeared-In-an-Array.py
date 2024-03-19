# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            pos = abs(num) - 1
            if nums[pos] > 0:
                nums[pos] = - nums[pos]

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans


# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans, mapping = [], {}

        for item in nums:
            mapping[item] = 1 if item in mapping else 0
        
        for i in range(1, len(nums) + 1):
            if i not in mapping:
                ans.append(i)
                
        return ans
