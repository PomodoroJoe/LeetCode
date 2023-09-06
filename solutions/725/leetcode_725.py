#------------------------------------------------------
# Solution 1 - helper array
#------------------------------------------------------

# Runtime:  80.18%
# Memory:   57.88%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = []

        nodes = []  
        node = head

        while node:
            nodes.append(node)
            node = node.next

        node_count = len(nodes)
        segment_count = node_count // k
        segment_extra = node_count % k

        index = 0
        while index < node_count:
            start = index
            end = index + segment_count

            if segment_extra:
                end += 1
                segment_extra -= 1

            nodes[end - 1].next = None
            result.append(nodes[start])
            index = end

        while len(result) < k:
            result.append(None)

        return result