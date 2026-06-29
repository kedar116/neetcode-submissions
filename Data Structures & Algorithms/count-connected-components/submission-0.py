class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        for i in range(n):
            adjList[i]=[]
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()
        components = 0

        def dfs(node):
            visit.add(node)
            for nei in adjList[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                components+=1
                dfs(i)

        return components