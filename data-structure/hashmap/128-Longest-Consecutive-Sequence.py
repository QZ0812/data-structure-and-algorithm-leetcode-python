# time/space O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count, ans = set(nums), 0
            
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


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  
        nums, result = set(nums), 0
        
        for num in nums:
            current_seq = 1
            if num-1 not in nums:
                while num+1 in nums:
                    current_seq+=1
                    num+=1
                    
            result = max(result, current_seq)
            
        return result
