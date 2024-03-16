class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, pre, cur = 0, 0, 1
        
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                pre = cur
                cur = 1
            else:
                cur += 1
                
            if cur <= pre:
                count += 1
                
        return count
