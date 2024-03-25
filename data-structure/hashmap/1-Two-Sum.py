#time/space O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, val in enumerate(nums):
            if val in count:
                return [count[val], i]
            
            count[target - val] = i
