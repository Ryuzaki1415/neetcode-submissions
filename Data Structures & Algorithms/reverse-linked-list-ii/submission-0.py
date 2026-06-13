# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:


        Dummy=ListNode(0,head)
        curr=head
        prevleft=Dummy
        # reach the left-1 index
        for i in range(left-1):
            prevleft=curr
            curr=curr.next

        # now curr is at left and prevleft is at the left side of curr

        # now reverse

        prev=None

        # reverse right-left+1

        for i in range(right-left+1):

            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

        # now we need to clean-up the connections
        # we need the leftptr to point to the reversed node
        #now current points at the last node

        prevleft.next.next=curr
        # the prev pointer points to the reversed gead
        prevleft.next=prev


        return Dummy.next 



