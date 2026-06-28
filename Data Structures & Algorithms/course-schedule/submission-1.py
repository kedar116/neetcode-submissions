class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Topological sort
        inDegree = [0]*numCourses
        adjList = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            inDegree[pre]+=1
            adjList[crs].append(pre)

        q = deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)

        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for nei in adjList[node]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)

        return numCourses==finish