class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adjList = [[] for _ in range(n+1)]

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            visit = set()
            if not dfs(n1, -1):
                return [n1,n2]
        return []     