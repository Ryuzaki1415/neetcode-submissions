# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # so we need to remove the Nth node from the end.
        # to do that we need the length of the linked list

        Dummy=ListNode()
        Dummy.next=head
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1

        # now we have the length of the linked list.
        target_idx=length-n

        curr=Dummy
        for i in range(target_idx):
            curr=curr.next

        curr.next=curr.next.next

        return Dummy.next

            

        