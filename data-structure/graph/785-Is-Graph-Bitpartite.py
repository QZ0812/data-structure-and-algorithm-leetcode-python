# space O(N)    time O(v+u)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        
        flag, q = [0] * len(graph), []

        def dfs(i):
            if not flag[i]:
                flag[i] = 1
                q.append(i)
            while q:
                indx = q.pop(0)
                for node in graph[indx]:
                    if flag[node] == 0:
                        q.append(node)
                        flag[node] = 2 if flag[indx] == 1 else 1
                    else:
                        if flag[node] == flag[indx]:
                            return False     
            return True
                
        for i in range(len(graph)):
            if not dfs(i):
                return False
            
        return True
