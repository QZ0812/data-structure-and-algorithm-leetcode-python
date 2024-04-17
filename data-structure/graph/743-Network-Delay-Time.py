from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for sr, tg, time in times:
            graph[sr].append((tg, time))
         
        visited = set()
        minheap = [(0, k)]
        ans = 0
        
        while minheap:
            path, node = heappop(minheap)
            if node in visited:
                continue
            
            visited.add(node)
        
            for nd, pt in graph[node]:
                if nd not in visited:
                    heappush(minheap, (path + pt, nd))
            ans = max(ans, path)

        return ans if len(visited) == n else -1
