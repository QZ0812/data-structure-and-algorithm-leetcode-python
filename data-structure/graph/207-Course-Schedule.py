class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
            
        cycle, visit = set(), set()
        def dfs(item):
            if item in cycle:
                return False
            if item in visit:
                return True
            cycle.add(item)
            for itm in graph[item]:
                if not dfs(itm):
                    return False
            cycle.remove(item)
            visit.add(item)
            return True
                
        for i in range(numCourses):
            if dfs(i) == False:
                return False
            
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = [[] for _ in range(numCourses)]
        flag = [0] * numCourses
        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
            flag[prerequisites[i][1]] += 1

        q = []
        for i in range(len(flag)):
            if not flag[i]:
                q.append(i)
        
        while q:
            node = q.pop(0)
            for stf in graph[node]:
                flag[stf] -= 1
                if flag[stf] == 0:
                    q.append(stf)
                
        for item in flag:
            if item:
                return False
        return True
