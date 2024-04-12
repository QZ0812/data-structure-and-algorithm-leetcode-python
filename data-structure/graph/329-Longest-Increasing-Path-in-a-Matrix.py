# time O(N*M) space O(N*M)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        count = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        output = 1
        
        def dfs(i, j):
            if i < 0 or j < 0 or i > row - 1 or j > col - 1:
                return 0
            
            if count[i][j] != 0:
                return count[i][j]
            
            max_depth = 0
            if  i -1 >= 0 and matrix[i][j] < matrix[i -1][j]:
                max_depth = max(max_depth, dfs(i-1, j))
            if  i + 1 <= row - 1 and matrix[i][j] < matrix[i + 1][j]:
                max_depth = max(max_depth, dfs(i+1, j))
            if  j -1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                max_depth = max(max_depth, dfs(i, j-1))
            if  j + 1 <= col -1 and matrix[i][j] < matrix[i][j + 1]:
                max_depth = max(max_depth, dfs(i, j+1))
                
            count[i][j] = 1 + max_depth
            return 1 + max_depth
        
        row, col = len(matrix),  len(matrix[0])
        for i in range(row):
            for j in range(col):
                if count[i][j] == 0:
                    output = max(output, dfs(i, j))
                    
        return output
