# time/space O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count, ans = {}, 0
        
        for num in nums:
            count[num] = 1 if num not in count else count[num] + 1
            
        while count:
            curr, freq = count.popitem()
            pre, nex = curr - 1, curr + 1
            
            currfreq = freq
            while pre in count:
                ans = max(ans, currfreq + count[pre])
                currfreq = count.pop(pre)
                pre = pre - 1
            
            prefreq = freq 
            while nex in count:
                ans = max(ans, prefreq + count[nex])
                prefreq = count.pop(nex)
                nex = nex + 1
                
        return ans

# time/space O(n)
class Solution:
    def findLHS(self, nums: List[int]) -> int:   
        count, ans = {}, 0
        
        for num in nums:   
            count[num] = 1 if num not in count else count[num] + 1

        for key, value in count.items():
            if key+1 in count and count[key+1]+value > ans:
                ans = count[key+1]+value
                
        return ans
