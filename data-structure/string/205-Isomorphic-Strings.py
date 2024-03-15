# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # make sure it is one to one mapping
        if len(set(s))!= len(set(t)):
            return False
        
        rep, ans= {}, ""
        # make sure index match
        for i in range(len(s)):
            if s[i] not in rep:
                rep[s[i]] = t[i]
                ans += t[i]
            else:
                ans += rep[s[i]]
        
        return True if ans == t else False
