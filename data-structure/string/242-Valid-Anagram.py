# Time Complexity: O(n)
# Space Complexity: O(n)
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = defaultdict(int)
        
        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
            
        for v in count.values():
            if v != 0:
                return False
            
        return True
