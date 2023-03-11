#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  63.28%
# Memory:   26.39%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # Base Cases

        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        # Find Middle Node

        prev = head
        slow = head
        fast = head.next

        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next != None else None

        # Recurse

        root = TreeNode(slow.val)

        prev.next = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        prev.next = slow

        return root




#------------------------------------------------------
# Solution 1 - recursive (slightly cleaner)
#------------------------------------------------------

# Runtime:  68.18%
# Memory:   61.21%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        # Base Cases

        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        # Find Middle Node

        prev = head
        slow = head.next
        fast = head.next.next

        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Recurse

        mid = prev.next

        root = TreeNode(mid.val)

        root.right = self.sortedListToBST(mid.next)

        prev.next = None
        root.left = self.sortedListToBST(head)
        
        prev.next = mid

        return root
        