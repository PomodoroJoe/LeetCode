#------------------------------------------------------
# Solution 1 - stacks
#------------------------------------------------------

# Runtime:  56.64%
# Memory:   68.70%


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        stack_1 = []
        stack_2 = []

        node_1 = l1
        node_2 = l2

        while node_1:
            stack_1.append(node_1.val)
            node_1 = node_1.next

        while node_2:
            stack_2.append(node_2.val)
            node_2 = node_2.next

        carry = 0

        while stack_1 or stack_2 or carry:
            v1 = stack_1.pop(-1) if stack_1 else 0
            v2 = stack_2.pop(-1) if stack_2 else 0

            val = v1 + v2 + carry
            carry = 0

            if val >= 10:
                carry = 1
                val = val % 10

            result = ListNode(val, result)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  43.75%
# Memory:   31.82%


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        stack_1 = deque([])
        stack_2 = deque([])

        node_1 = l1
        node_2 = l2

        while node_1:
            stack_1.append(node_1.val)
            node_1 = node_1.next

        while node_2:
            stack_2.append(node_2.val)
            node_2 = node_2.next

        carry = 0

        while stack_1 or stack_2 or carry:
            v1 = stack_1.pop() if stack_1 else 0
            v2 = stack_2.pop() if stack_2 else 0

            val = v1 + v2 + carry
            carry = 0

            if val >= 10:
                carry = 1
                val = val % 10

            result = ListNode(val, result)

        return result