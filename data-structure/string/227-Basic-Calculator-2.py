class Solution:
    def calculate(self, s: str) -> int:
        s = s + "+"
        l, r, pre, ans = 0, 0, "+", []
        while l <= r and r < len(s):
            if s[r] in ['+', '-', '*', '/']:
                if pre == '+':
                    ans.append(int(s[l:r])) 
                elif pre == '-':
                    ans.append(int(s[l:r]) * (-1))
                elif pre == '*':
                    ans.append(int(s[l:r]) * ans.pop())
                else:
                    ans.append(int(ans.pop() / int(s[l:r])))

                pre = s[r]
                r += 1
                l = r
            else:
                r += 1
       
        return sum(ans)
