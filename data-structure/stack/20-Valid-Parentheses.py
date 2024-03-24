class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthese_mapping = {"(": ")", "{": "}", "[": "]"}
        
        for item in s:
            if item in ["(", "{", "["]:
                stack.append(item)
            elif item in [")", "}", "]"]:
                if not stack or parenthese_mapping[stack.pop()] != item:
                    return False
              
        return len(stack) == 0
