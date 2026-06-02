# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #min heap. Use counter for tie breaker between nodes
        # O(N*logk), O(k)
        minHeap=[]
        counter=0

        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, counter, node))
                counter+=1

        dummy=ListNode(0)
        curr=dummy

        while minHeap:
            value, index, smallestNode = heapq.heappop(minHeap)
            curr.next = smallestNode
            curr=curr.next

            if smallestNode.next:
                heapq.heappush(minHeap, (smallestNode.next.val, counter, smallestNode.next))
                counter+=1

        return dummy.next
