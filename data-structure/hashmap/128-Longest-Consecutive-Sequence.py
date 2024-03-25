# time/space O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count, ans = set(), 0
        for num in nums:
            count.add(num)
            
        while count:
            curr = count.pop()
            pre, nex = curr -1, curr + 1
            
            while pre in count:
                count.remove(pre)
                pre = pre -1
                
            while nex in count:
                count.remove(nex)
                nex = nex + 1
                
            ans = max(ans, nex - pre - 1)
            
        return ans
