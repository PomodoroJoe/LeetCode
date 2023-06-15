#------------------------------------------------------
# Solution 1 - level order traversal w/ double buffer
#------------------------------------------------------

# Runtime:  89.65%
# Memory:   67.41%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = 1

        level = [root]
        next_level = []

        maximal = root.val
        level_count = 0

        while level:
            next_level = []
            level_sum = 0
            level_count += 1

            for node in level:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)

            if level_sum > maximal:
                maximal = level_sum
                result = level_count

            level = next_level

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ inline ifs
#------------------------------------------------------

# Runtime:  91.17%
# Memory:   24.67%


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        result = 1

        level = [root]
        next_level = []

        maximal = root.val
        level_count = 0

        while level:
            next_level = []
            level_sum = 0
            level_count += 1

            for node in level:
                level_sum += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)

            if level_sum > maximal:
                maximal = level_sum
                result = level_count

            level = next_level

        return result