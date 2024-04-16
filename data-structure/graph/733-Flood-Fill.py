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
