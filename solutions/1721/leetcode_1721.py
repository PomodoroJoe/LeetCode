#------------------------------------------------------
# Solution 1 - swap nodes
#------------------------------------------------------

# Runtime:  42.52%
# Memory:   22.68%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1_prev = None
        n1 = head
        n1_next = None

        n2_prev = None
        n2 = None
        n2_next = None

        node = head
        count = 1

        while count < k:
            n1_prev = n1
            n1 = n1.next
            node = node.next
            count += 1

        n2 = head

        while node.next != None:
            n2_prev = n2
            n2 = n2.next
            node = node.next

        n1_next = n1.next
        n2_next = n2.next

        # swap

        if n1_prev:
            n1_prev.next = n2
        n2.next = n1_next if n1_next != n2 else n1

        if n2_prev:
            n2_prev.next = n1
        n1.next = n2_next if n2_next != n1 else n2

        if n1 == head:
            return n2

        if n2 == head:
            return n1

        return head



#------------------------------------------------------
# Solution 2 - swap Vals
#------------------------------------------------------

# Runtime:  97.61%
# Memory:   22.68%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n1 = None
        n2 = None

        node = head
        count = 1

        while count < k:
            node = node.next
            count += 1

        n1 = node
        node = node.next

        n2 = head
        while node != None:
            n2 = n2.next
            node = node.next

        n1.val, n2.val = n2.val, n1.val

        return head