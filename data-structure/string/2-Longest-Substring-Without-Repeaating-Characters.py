# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, ans, count = 0, 0, set()
        
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l += 1
                    
            count.add(s[r])
            ans = max(ans, r - l + 1)

        return ans
