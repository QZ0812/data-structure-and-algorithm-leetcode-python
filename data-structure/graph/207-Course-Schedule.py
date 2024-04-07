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
