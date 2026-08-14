# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val ,i, lists[i]))

        dummy = ListNode()
        curr = dummy
        while minHeap:
            val, _,node = heapq.heappop(minHeap)
            curr.next = node
            curr=curr.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val , i, node.next))
                i+=1
        return dummy.next

