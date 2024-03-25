# time/space O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, q = [], []
        l = r = 0
        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            
            if r + 1 >= k:
                ans.append(q[0])
                if nums[l] == q[0]:
                    q.pop(0)
                l += 1
              
            r += 1
        return ans
