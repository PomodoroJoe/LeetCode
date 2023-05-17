#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  22.30%
# Memory:    7.94%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n0 = None
        n1 = head
        n2 = None
        n3 = None

        result = head.next

        # swap

        # n0 --> n1 --> n2 --> n3
        # n0 --> n2 --> n1 --> n3

        # n0 --> n2 --> n1 --> n3 --> n4 --> n5
        #                      ^ 

        while n1 and n1.next:
            n2 = n1.next
            n3 = n2.next

            if n0:
                n0.next = n2
            n2.next = n1
            n1.next = n3

            n0 = n1
            n1 = n3

        return result
