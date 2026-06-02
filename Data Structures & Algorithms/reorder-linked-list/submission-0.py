# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find midpoint
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #Break the list
        second=slow.next
        slow.next=None
        #Reverse second list
        prev,curr=None,second
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        #New head
        second=prev
        #Merge both lists
        first = head
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2


        
