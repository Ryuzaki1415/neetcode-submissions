# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        # the plan is to find the center of the Linkedlist
        # reverse the second part of Linked list
        # Traverse the Linked list one from the head and another from previous
        # then make a new Linked list

        # now to find the center we need the floyds hare and tortoise algorithm


        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # ath the end, slow will be the midpoint.

        curr=slow.next
        prev=None
        slow.next=None

        while curr :
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp


        # so now prev is the new head of the Linked list

        first_ptr=head
        second_ptr=prev


        while second_ptr:

            temp1=first_ptr.next
            temp2=second_ptr.next

            first_ptr.next=second_ptr
            second_ptr.next=temp1
            first_ptr=temp1
            second_ptr=temp2

        