# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy

        while True:
            minNode=None
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode is None or lists[minNode].val > lists[i].val:
                    minNode=i

            if minNode is None:
                break

            curr.next=lists[minNode]
            lists[minNode]=lists[minNode].next
            curr=curr.next

        return dummy.next