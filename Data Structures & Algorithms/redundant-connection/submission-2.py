class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        inDegree = [0] * (n+1)
        adjList = [[] for _ in range(n+1)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            inDegree[u]+=1
            inDegree[v]+=1

        q = deque()
        for i in range(1,n+1):
            if inDegree[i]==1:
                q.append(i)

        while q:
            node = q.popleft()
            inDegree[node]-=1
            for nei in adjList[node]:
                inDegree[nei]-=1
                if inDegree[nei]==1:
                    q.append(nei)
        
        for u,v in reversed(edges):
            if inDegree[u]>0 and inDegree[v]>0:
                return [u,v]
        return []