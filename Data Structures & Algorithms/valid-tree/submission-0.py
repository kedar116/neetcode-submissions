class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjList = {}
        for i in range(n):
            adjList[i]=[]
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visit = set()
        def dfs(node,prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if nei ==prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True

        return dfs(0,-1) and n ==len(visit)

