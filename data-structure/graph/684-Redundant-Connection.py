#Time complexity: O(n) for creating n single item sets . The two techniques -path compression with the union by rank/size, the time complexity will reach nearly constant time. It turns out, that the final amortized time complexity is O(α(n)), where α(n) is the inverse Ackermann function, which grows very steadily (it does not even exceed for n<10600  approximately).
#Space complexity: O(n) because we need to store n elements in the Disjoint Set Data Structure.
# Union Find: https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        
        if irep == jrep:
            return False
        
        if self.rank[i] < self.rank[j]:
            self.parent[jrep] = irep
            self.rank[j] += self.rank[i]
        else:
            self.parent[irep] = jrep
            self.rank[i] += self.rank[j]
            
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for n1, n2 in edges:
            if not uf.union(n1-1, n2-1):
                return [n1, n2]
