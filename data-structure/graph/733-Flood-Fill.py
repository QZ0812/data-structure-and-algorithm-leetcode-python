#bfs
# time O(x*y) space O(n)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        row, col, visited = len(image), len(image[0]), set()
        
        q = [(sr, sc)]
        while q:
            r, c = q.pop()
            visited.add((r, c))
            if r - 1 >= 0 and image[r-1][c] == image[sr][sc] and (r-1,c) not in visited:
                q.append((r-1, c))
            if r + 1 <= row -1 and image[r+1][c] == image[sr][sc] and (r+1,c) not in visited:
                q.append((r+1, c))
            if c - 1 >= 0 and image[r][c-1] == image[sr][sc] and (r, c-1) not in visited:
                q.append((r, c-1))
            if c + 1 <= col-1 and image[r][c+1] == image[sr][sc] and (r, c+1) not in visited:
                q.append((r, c+1))
                
        for r, c in visited:
            image[r][c] = color
            
        return image


# dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col, visited = len(image), len(image[0]), set()
        starting_color = image[sr][sc]
        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            if image[i][j] != starting_color or (i, j) in visited:
                return
            
            visited.add((i, j))
            image[i][j] = color
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        dfs(sr, sc)
        return image
