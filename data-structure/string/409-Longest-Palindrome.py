class Solution:
    def longestPalindrome(self, s: str) -> int:
        count, ans = {}, 0
        
        for item in s:
            count[item] = 1 if item not in count else count[item] + 1
            
        for v in count.values():
            if v % 2 != 0:
                ans += 1
                
        return len(s) if ans == 0 else len(s)  - ans + 1
