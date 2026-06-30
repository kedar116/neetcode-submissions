class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Optimal DFS
        n = len(edges)
        adjList = [[] for _ in range(n+1)]
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visit = set()
        cycle = set()
        cycleStart=-1

        def dfs(node, prev):
            nonlocal cycleStart
            if node in visit:
                cycleStart = node
                return True
            visit.add(node)
            for nei in adjList[node]:
                if nei ==prev:
                    continue
                if dfs(nei, node):
                    if cycleStart!=-1:
                        cycle.add(node)
                    if node ==cycleStart:
                        cycleStart=-1
                    return True
            return False

        dfs(1,-1)

        for n1,n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1,n2]
        return []