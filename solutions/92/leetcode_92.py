#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  33.89%
# Memory:   31.20%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        count = 1

        # return new_list_head
        def reverseSegment(pre_start_node, start_node, end_node, post_end_node):
            if pre_start_node:
                pre_start_node.next = None
            end_node.next = None

            node = start_node
            prev_node = None

            while node:
                temp_node = node.next
                node.next = prev_node
                prev_node = node
                node = temp_node

            if pre_start_node:
                pre_start_node.next = end_node

            start_node.next = post_end_node

            return end_node


        pre_start_node = None
        start_node = None
        end_node = None
        post_end_node = None

        prev_node = None

        while node:
            if count == left:
                pre_start_node = prev_node
                start_node = node

            if count == right:
                end_node = node
                post_end_node = node.next

            prev_node = node
            node = node.next
            count += 1


        new_head = reverseSegment(pre_start_node, start_node, end_node, post_end_node)
        return new_head if pre_start_node == None else head



#------------------------------------------------------
# Solution 2 - Solution 1 w early out of discovery loop
#------------------------------------------------------

# Runtime:  73.24%
# Memory:   91.50%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        count = 1

        # return new_list_head
        def reverseSegment(pre_start_node, start_node, end_node, post_end_node):
            if pre_start_node:
                pre_start_node.next = None
            end_node.next = None

            node = start_node
            prev_node = None

            while node:
                temp_node = node.next
                node.next = prev_node
                prev_node = node
                node = temp_node

            if pre_start_node:
                pre_start_node.next = end_node

            start_node.next = post_end_node

            return end_node


        pre_start_node = None
        start_node = None
        end_node = None
        post_end_node = None

        prev_node = None

        while node and count <= right:
            if count == left:
                pre_start_node = prev_node
                start_node = node

            if count == right:
                end_node = node
                post_end_node = node.next

            prev_node = node
            node = node.next
            count += 1


        new_head = reverseSegment(pre_start_node, start_node, end_node, post_end_node)
        return new_head if pre_start_node == None else head