#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  85.76%
# Memory:   27.83%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generateTreesRecurse(start_num, n):
            if n == 0:
                return [None]

            if n == 1:
                return [TreeNode(start_num)]

            k = n - 1

            result = []

            for left_count in range(n):
                root_val = start_num + left_count
                left = generateTreesRecurse(start_num, left_count)

                right_count = k - left_count
                start_right = root_val + 1
                right = generateTreesRecurse(start_right, right_count)

                for left_option in left:
                    for right_option in right:
                        option = TreeNode(root_val, left_option, right_option)
                        result.append(option)

            return result

        return generateTreesRecurse(1, n)



#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper vars
#------------------------------------------------------

# Runtime:  97.94%
# Memory:   45.85%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generateTreesRecurse(start_num, n):
            if n == 0:
                return [None]

            if n == 1:
                return [TreeNode(start_num)]

            k = n - 1

            result = []

            for left_count in range(n):
                root_val = start_num + left_count
                left = generateTreesRecurse(start_num, left_count)
                right = generateTreesRecurse(root_val + 1, k - left_count)

                for left_option in left:
                    for right_option in right:
                        option = TreeNode(root_val, left_option, right_option)
                        result.append(option)

            return result

        return generateTreesRecurse(1, n)