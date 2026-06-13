# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # to get the nth node, we need the length of the Linked list


        length=0

        curr=head

        while curr:
            length+=1
            curr=curr.next

        # now we have the length
        # now we need to find the element to remove

        target_index=length-n
        Dummy=ListNode(0)
        Dummy.next=head
        curr=Dummy
        index=0
        while curr:
            # check if the index is at the target
            if index==target_index:
                #remove the element
                curr.next=curr.next.next
            index+=1
            curr=curr.next
        
        return Dummy.next











