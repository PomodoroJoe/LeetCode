#------------------------------------------------------
# Solution 1 - tail list
#------------------------------------------------------

# Runtime:  74.36%
# Memory:   55.21%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        result = head

        prev = None
        node = head

        tail_list_head = None
        tail_list_tail = None

        while node:
            if node.val >= x:
                next_node = node.next

                if prev:
                    prev.next = next_node
                else:
                    result = next_node
                node.next = None

                if not tail_list_head:
                    tail_list_head = node
                    tail_list_tail = node
                else:
                    tail_list_tail.next = node
                    tail_list_tail = node

                node = next_node
            else:
                prev = node
                node = node.next

        if prev:
            prev.next = tail_list_head
        else:
            result = tail_list_head

        return result


#------------------------------------------------------
# Solution 2 - left and right lists
#------------------------------------------------------

# Runtime:  74.36%
# Memory:   14.68%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = None
        left_tail = None

        right_head = None
        right_tail = None

        node = head

        while node:
            next_node = node.next
            node.next = None

            if node.val >= x:
                if not right_head:
                    right_head = node
                    right_tail = node
                else:
                    right_tail.next = node
                    right_tail = node
            else:
                if not left_head:
                    left_head = node
                    left_tail = node
                else:
                    left_tail.next = node
                    left_tail = node

            node = next_node

        if left_tail:
            left_tail.next = right_head
        else:
            left_head = right_head

        return left_head


#------------------------------------------------------
# Solution 3 - Solution 2 (optimized)
#------------------------------------------------------

# Runtime:  91.69%
# Memory:   83.82%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = None
        left_tail = None

        right_head = None
        right_tail = None

        node = head

        while node:
            next_node = node.next
            node.next = None

            if node.val < x:
                if left_head:
                    left_tail.next = node
                    left_tail = node
                else:
                    left_head = node
                    left_tail = node
            else:
                if right_head:
                    right_tail.next = node
                    right_tail = node
                else:
                    right_head = node
                    right_tail = node

            node = next_node

        if left_tail:
            left_tail.next = right_head
        else:
            left_head = right_head

        return left_head