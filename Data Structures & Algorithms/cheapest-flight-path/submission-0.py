class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minHeap = [] #cost,node,stops
        adjList = [[] for _ in range(n)]
        distances = [[float("inf")]*(k+2) for _ in range(n)] #[node][edges]
        
        for u,v,w in flights:
            adjList[u].append((v,w))

        distances[src][0]=0 
        heapq.heappush(minHeap,(0,src,0))

        while minHeap:
            cost,node,edges = heapq.heappop(minHeap)
            if distances[node][edges]<cost:
                continue
            if node==dst:
                return cost
            if edges==k+1: 
                continue
            for nei,w in adjList[node]:
                nextCst = cost+w
                newEdges = 1+edges
                if distances[nei][newEdges]>nextCst:
                    distances[nei][newEdges] = nextCst
                    heapq.heappush(minHeap, (nextCst,nei,newEdges))
        return -1

