class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rm, cm = len(mat), len(mat[0])
        if rm*cm != r*c:
            return mat
        
        output = [[0]*c for _ in range(r)]
        
        count = 0
        for i in range(rm):
            for j in range(cm):
                count += 1
                ro = (count -1)//c 
                co = count - ro*c -1
                output[ro][co] = mat[i][j]
                
        return output
