# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        length=0
        while curr:
            length+=1
            curr=curr.next
        
        steps=length-n
        dummy=ListNode(0,head)
        prev=dummy

        for _ in range(steps):
            prev=prev.next
        
        temp=prev.next
        prev.next=temp.next
        temp.next=None

        return dummy.next



