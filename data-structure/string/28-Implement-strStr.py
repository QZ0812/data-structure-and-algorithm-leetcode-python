# Time Complexity: O(n*m)
# Space Complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, ans =0, -1
        lenh, lenn = len(haystack), len(needle)

        while i < lenh - lenn + 1:
            if haystack[i] == needle[0] and haystack[i: i+lenn] == needle:
                ans = i
                break
            i += 1

        return ans
