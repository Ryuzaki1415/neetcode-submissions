# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # for linked list cycle  we basically need FLoyds hare and tortoise algorithm
        
        slow=head
        fast=head


        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            # if there is a cycle, then both meet,

            if slow==fast:
                return True

        
        return False
        