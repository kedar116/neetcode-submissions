# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        group=0
        while curr and group<k:
            curr=curr.next
            group+=1

        if group<k:
            return head

        if group==k:
            res=self.reverseKGroup(curr,k)
            prev,curr = res,head
            while group>0:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                group-=1

            head=prev

        return head



                
                