# time/space O(v+E)
# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])

        stack = []
        visit, cycle = set(), set()

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            
            cycle.add(i)
            for gh in graph[i]:
                if not dfs(gh):
                    return False
            visit.add(i)
            cycle.remove(i)
            stack.append(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans
