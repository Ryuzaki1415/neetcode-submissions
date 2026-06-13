# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        # to add two numbers remember the carry
        carry=0
        # since the linked list is in reverse, we can add direclty

        Dummy=ListNode(0)
        curr=Dummy
        while l1 or l2 or carry:
            # handle varying length cases
            # if l1 exists, get its val or return 0 
            if l1:
                val1=l1.val
            else:
                val1=0

            # similarly if l2 exists then we get the val else 0
            if l2:
                val2=l2.val
            else:
                val2=0

            # total value is l1+l2+carry
            total=val1+val2+carry
            #the digit to be added to the result is the ones place.
            # the new carry is total//10
            carry=total//10
            total=total%10
            curr.next=ListNode(total)


            # to update the pointers

            curr=curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return Dummy.next







        