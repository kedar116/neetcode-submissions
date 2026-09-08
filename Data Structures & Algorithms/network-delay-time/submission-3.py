class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n+1)]
        minHeap = []
        min_times = [float("inf")]*(n+1)
        min_times[k]=0

        for u,v,t in times:
            adjList[u].append((v,t))

        heapq.heappush(minHeap,(0,k)) #(time,node)
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if time > min_times[node]:
                continue
            for nei,t in adjList[node]:
                if time+t<min_times[nei]:
                    min_times[nei] = time+t
                    heapq.heappush(minHeap,(time+t,nei))

        ans = max(min_times[1:])
        return ans if ans!=float("inf") else -1 