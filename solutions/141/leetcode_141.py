#------------------------------------------------------
# Solution 1 - seen set
#------------------------------------------------------

# Runtime:  94.80%
# Memory:    8.53%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        node = head
        while node != None and node not in seen:
            seen.add(node)
            node = node.next

        return node != None



#------------------------------------------------------
# Solution 3 - fast & slow
#------------------------------------------------------

# Runtime:  88.45%
# Memory:   48.57%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None

        while fast and slow != fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        return fast != None