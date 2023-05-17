#------------------------------------------------------
# Solution 1 - non-destructive (of input list)
#------------------------------------------------------

# Runtime:  23.17%
# Memory:   13.90%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = 0

        n_1 = None
        n0 = None
        n1 = head
        n2 = head.next

        while n2.next:
            n0 = n1
            n1 = n1.next
            n2 = n2.next.next

            n0.next = n_1
            n_1 = n0

        # n1 = just left of mid point

        n2 = n1.next

        result = n1.val + n2.val

        n_1 = n2
        n1 = n0
        n2 = n2.next        

        while n1 and n2:
            result = max(result, n1.val + n2.val)

            n0 = n1
            n1 = n1.next
            n2 = n2.next

            n0.next = n_1
            n_1 = n0

        return result



#------------------------------------------------------
# Solution 2 - destructive (of input list)
#------------------------------------------------------

# Runtime:  99.10%
# Memory:   85.34%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = 0

        n_1 = None
        n0 = None
        n1 = head
        n2 = head.next

        while n2.next:
            n0 = n1
            n1 = n1.next
            n2 = n2.next.next

            n0.next = n_1
            n_1 = n0

        n2 = n1.next
        n1.next = n0

        result = n1.val + n2.val

        while n1 and n2:
            result = max(result, n1.val + n2.val)
            n1 = n1.next
            n2 = n2.next

        return result