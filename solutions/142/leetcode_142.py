#------------------------------------------------------
# Solution 1 - set
#------------------------------------------------------

# Runtime:  91.37%
# Memory:   08.69%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()

        node = head
        while node and node not in nodes:
            nodes.add(node)
            node = node.next

        return node



#------------------------------------------------------
# Solution 2 - fast/slow pointers w/ diagram
#------------------------------------------------------

# Runtime:  63.16%
# Memory:   90.47%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None:
            slow = slow.next
            fast = fast.next.next if fast.next != None else None

            if fast == slow:
                break

        if fast == None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

        
        # H |--------------------|M|--------------------| T

        # H |--------------------|M|--------------------| T
        #   ^
        #   FS

        # H |--------------------|M|--------------------| T
        #           ^       ^
        #           S       F

        # H |--------------------|M|--------------------| T
        #                         ^                       ^
        #                         S                       F


        # H |---------C----------|M|----------M---------| T
        #             ^           ^
        #             F           S


        # H |---------C----------|M|----------M---------| T
        #                                     ^
        #                                     FS
        #                        |M|--------->|
        #                               x
        #             |----------|M|--------->|
        #                        2x
        #
        #             |<---------|M|--------->|
        #                   x            x
        #
        # H |--------------------|M|--------------------| T
        #   |-------->|<---------|M|--------->|<--------|
        #       y           x           x           y
        #
        # H |--------------------|M|----------M---------| T
        #                                     ^
        #                                    FS ------->| T
        # H |-------->|c                             y
        #       y



#------------------------------------------------------
# Solution 3 - fast/slow pointers w/o diagram
#------------------------------------------------------

# Runtime:  93.39%
# Memory:   52.59%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast != None:
            slow = slow.next
            fast = fast.next.next if fast.next != None else None

            if fast == slow:
                break

        if fast == None:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow