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

        def bfs(node):
            q = deque()
            q.append(node)
            visit.add(node)
            while q:
                curr = q.popleft()
                for nei in adjList[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

        for i in range(n):
            if i not in visit:
                components+=1
                bfs(i)

        return components