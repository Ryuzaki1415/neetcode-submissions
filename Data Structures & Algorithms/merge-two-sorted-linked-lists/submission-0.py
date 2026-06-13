# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # to merge two sorted linked lists,
        Dummy=ListNode()
        curr=Dummy
        # while the list 1 and list 2 contains elements
        while list1 and list2:

            # if the val in list1 is greater then add it to the dummy LL
            if list1.val>list2.val:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next

            #after one addition move the ptr
            curr=curr.next
            

        # now if one finishes we just add the rest?

        if list1:
            curr.next=list1
        if list2:
            curr.next=list2
        
        return Dummy.next

        