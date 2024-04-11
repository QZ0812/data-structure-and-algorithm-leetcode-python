#Time complexity: O(N * E)
#N is number of queries
#E is number of edges or simple number of equations
#Space complexity: O(E)
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i, eq in enumerate(equations):
            graph[eq[0]].append((eq[1],  values[i]))
            graph[eq[1]].append((eq[0],  1/values[i]))
                
        def dfs(start, end):
            if start not in graph or end not in graph:
                return -1
            
            q = [(start, 1)]
            visit = set([start])
            while q:
                char, val = q.pop(0)
                if char == end:
                    return val
                for nei, weight in graph.get(char):
                    if nei not in visit:
                        q.append([nei, val*weight])
                        visit.add(nei)
            return -1
                     
        ans = []        
        for query in queries:
            ans.append(dfs(query[0], query[1]))
            
        return ans
