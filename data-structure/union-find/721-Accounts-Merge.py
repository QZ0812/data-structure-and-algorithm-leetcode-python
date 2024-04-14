class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        
        if jrep == irep:
            return
            
        if self.rank[jrep] < self.rank[irep]:
            self.parents[jrep] = irep
        elif self.rank[jrep] > self.rank[irep]:
            self.parents[irep] = jrep 
        else:
            self.parents[irep] = jrep
            self.rank[jrep] = self.rank[irep] + 1
        
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
