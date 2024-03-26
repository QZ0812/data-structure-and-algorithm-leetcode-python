# time/space O(n)
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq, ans, count = 1, len(nums), {}
        
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = [i]  
            else:
                count[num].append(i)

        for k, v in count.items():
            if freq < len(v):
                freq = len(v)
                ans= v[-1]-v[0]
            elif freq == len(v):
                ans= min(ans, v[-1]-v[0])
                
        return ans + 1 if ans < len(nums) else 1
