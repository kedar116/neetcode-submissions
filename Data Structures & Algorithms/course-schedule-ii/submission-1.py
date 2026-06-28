class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        inDegree=[0]*numCourses
        for crs, pre in prerequisites:
            inDegree[pre]+=1
            adjList[crs].append(pre)

        finish, output = 0, []
        q = deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            output.append(node)
            finish+=1
            for nei in adjList[node]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)

        if finish !=numCourses:
            return []
        return output[::-1]