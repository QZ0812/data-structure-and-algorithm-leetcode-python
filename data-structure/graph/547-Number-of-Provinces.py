# time O(n*n), space O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities_num, visit, count = len(isConnected), set(), 0
        
        def dfs(i, isConnected):
            if i in visit:
                return
            
            visit.add(i)
            for j in range(cities_num):
                if j not in visit and i != j and isConnected[i][j] == 1:
                    dfs(j, isConnected)
        
        for i in range(cities_num):
            if i not in visit:
                dfs(i, isConnected)
                count += 1
                
        return count
