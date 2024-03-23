# Time Complexity: O(n*m)
# Space Complexity: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m, n = len(matrix), len(matrix[0]) 
        i, j = 0 , n - 1
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1    
            else:
                i += 1
                      
        return False
