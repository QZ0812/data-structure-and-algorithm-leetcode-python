# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            count += self.subStrings(i, i, s)        //odd lenght
            count += self.subStrings(i, i + 1, s)    //even length
        return count
    
    def subStrings(self, l, r ,s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
                
        return count


# brute force
#O(n^2) start - end pairs and O(n) palindromic checks
# Time Complexity: O(n^3)
# Space Complexity: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        i, j, count = 0, 0, 0
        
        while i < len(s):
            while j < len(s):
                if self.is_palindromic(s[i:j+1]):
                    count += 1
                j += 1
              
            i += 1
            j = i
        
        return count
        
    def is_palindromic(self, s):
        if s[:] == s[::-1]:
            return True
        return False
