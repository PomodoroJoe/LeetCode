#------------------------------------------------------
# Solution 1 - merge all input lists into one result list
#------------------------------------------------------

# Runtime:  14.25%
# Memory:   55.21%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) < 2:
            return lists[0]

        def mergeLists(list_1, list_2):
            if not list_1:
                return list_2
            
            if not list_2:
                return list_1

            result_head = ListNode()    #<-- placeholder
            result_tail = result_head

            while list_1 and list_2:
                if list_1.val < list_2.val:
                    result_tail.next = list_1
                    list_1 = list_1.next
                else:
                    result_tail.next = list_2
                    list_2 = list_2.next
                    
                result_tail = result_tail.next

            result_tail.next = list_2 if list_2 else list_1
            return result_head.next

        
        result = None

        for current_list in lists:
            result = mergeLists(result, current_list)

        return result



#------------------------------------------------------
# Solution 2 - merge input lists together 2 at a time
#------------------------------------------------------

# Runtime:  67.65%
# Memory:   46.85%


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) < 2:
            return lists[0]

        def mergeLists(list_1, list_2):
            if not list_1:
                return list_2
            
            if not list_2:
                return list_1

            result_head = ListNode()    #<-- placeholder
            result_tail = result_head

            while list_1 and list_2:
                if list_1.val < list_2.val:
                    result_tail.next = list_1
                    list_1 = list_1.next
                else:
                    result_tail.next = list_2
                    list_2 = list_2.next
                    
                result_tail = result_tail.next

            result_tail.next = list_2 if list_2 else list_1
            return result_head.next

        
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                list_2 = lists[i + 1] if i + 1 < len(lists) else None

                new_list = mergeLists(list_1, list_2)
                new_lists.append(new_list)

            lists = new_lists

        return lists[0]