# time/space complexity O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nsum, ans, sum_map = 0, 0,{}
        
        for num in nums:
            nsum += num
            if nsum in sum_map:
                ans += sum_map[nsum]
            if nsum == k:
                ans += 1
            sum_map[nsum+k] = 1 if nsum+k not in sum_map else sum_map[nsum+k] + 1
        return ans
