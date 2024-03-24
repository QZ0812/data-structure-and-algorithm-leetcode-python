class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, ans = [], [0] *len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_val, stack_index = stack.pop()
                ans[stack_index] = i - stack_index
            stack.append((temp, i))
            
        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lenth = len(temperatures)
        ans = [0] *lenth
        
        for i in range(1, lenth):
            j = i
            while j < lenth and temperatures[i - 1] >= temperatures[j]:
                j += 1
            
            if j != lenth:
                ans[i - 1] = j - i + 1
        
        return ans
