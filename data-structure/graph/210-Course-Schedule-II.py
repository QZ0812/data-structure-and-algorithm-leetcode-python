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


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        visit = [0] * numCourses
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            visit[prerequisites[i][0]] += 1

        stack, ans = [], []
        for i in range(numCourses):
            if not visit[i]:
                stack.append(i)
                
        while stack:
            cur = stack.pop(0)
            ans.append(cur)
            for i in graph[cur]:
                visit[i] -= 1
                if not visit[i]:
                    stack.append(i)
                    
        for i in range(len(visit)):
            if visit[i]:
                return []
        return ans
