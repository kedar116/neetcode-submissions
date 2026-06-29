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
        q = deque()
        q.append((0,-1))
        visit.add(0)
        while q:
            node, prev = q.popleft()
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)
                q.append((nei, node)) 


        return n ==len(visit)

