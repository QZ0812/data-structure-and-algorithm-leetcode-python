class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n, ans, cur_max = len(arr), 0, 0
        
        for i in range(n):
            cur_max = max(arr[i], cur_max)
            if i == cur_max:
                ans += 1

        return ans
