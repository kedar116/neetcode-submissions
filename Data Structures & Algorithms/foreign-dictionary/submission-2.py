class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adjList, inDegree = {}, {}
        for word in words:
            for ch in word:
                if ch not in adjList:
                    adjList[ch] = set()
                    inDegree[ch] = 0

        for i in range(n-1):
            w1,w2 = words[i],words[i+1]
            min_iter = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:min_iter] == w2[:min_iter]:
                return ""
            for j in range(min_iter):
                if w1[j]!=w2[j]:
                    if w2[j] not in adjList[w1[j]]:
                        adjList[w1[j]].add(w2[j])
                        inDegree[w2[j]]+=1
                    break

        q = deque()
        for c in inDegree:
            if inDegree[c]==0:
                q.append(c)

        output = []
        while q:
            node = q.popleft()
            output.append(node)
            for nei in adjList[node]:
                inDegree[nei]-=1
                if inDegree[nei]==0:
                    q.append(nei)

        if len(output)!=len(inDegree):
            return ""

        return "".join(output)
