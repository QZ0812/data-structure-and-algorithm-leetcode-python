# time O(n*n)  space O(n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col, count = len(grid), len(grid[0]), 0
        visit = [[False] * col for _ in range(row)]
        
        def bfs(i, j):
            if i < 0 or i > row-1 or j < 0 or j > col-1:
                return
            if visit[i][j] or grid[i][j] == "0":
                return
            
            visit[i][j] = True

            if i - 1 >= 0 and grid[i-1][j] == "1":
                bfs(i-1, j)
            if i + 1 < row and grid[i+1][j] == "1":
                bfs(i+1, j)
            if j - 1 >= 0 and grid[i][j-1] == "1":
                bfs(i, j-1)
            if j + 1 < col and grid[i][j+1] == "1":
                bfs(i, j+1)
        
        for i in range(row):
            for j in range(col):
                if not visit[i][j]:
                    bfs(i, j)
                    if grid[i][j] == "1":
                        count += 1
                    
        return count
