# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:



        # We need a dummy Node to avoid edge cases such as when the first node is also included in the reversal and the head changes.

        Dummy=ListNode(0,head)
        prevleft=Dummy
        curr=head
         #phase 1 -> get to the left pointer


        # now we need the prevleft pointer to be at left-1 and curr to be at left

        for i in range(0,left-1):
            prevleft=curr
            curr=curr.next

        prev=None
        # now that we are at the start of the place to be reversed, reverse the array
        for i in range(right-left+1):

            temp=curr.next
            curr.next=prev

            prev=curr
            curr=temp

        
        #now at the reversed array, prevleft points towards just before the reversed array start
        #right pointer is at the end of the array
        prevleft.next.next=curr
        prevleft.next=prev

        return Dummy.next

