

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            ans = max(self.palindromicSubstring(i, i, s), self.palindromicSubstring(i, i + 1, s), ans, key=len)
            
        return ans
    
    def palindromicSubstring(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            
        return s[l+1:r]
