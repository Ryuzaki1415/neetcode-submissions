# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # okay to re-order list, we need to first find the center point,
        # then reverse the secpond part
        # and then iteratively make the final array

        # to find the center

        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # at the end of this slow.next is the starting of the second part

        second_head=slow.next
        slow.next=None
        prev=None


        while second_head:
            temp=second_head.next
            second_head.next=prev
            prev=second_head
            second_head=temp



        # now the head for the second LL is at prev

        first_head=head
        second_head=prev


        while second_head:
            temp1=first_head.next
            temp2=second_head.next

            first_head.next=second_head
            second_head.next=temp1
            first_head=temp1
            second_head=temp2
        

      

        
        


        