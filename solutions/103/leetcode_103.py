#------------------------------------------------------
# Solution 1 - iterative
#------------------------------------------------------

# Runtime:  52.10%
# Memory:   48.21%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        level = [root]
        next_level = []

        level_result = []
        left_to_right = True

        while level:
            node = level.pop(0)

            if node:
                level_result.append(node.val)
                next_level += [node.left, node.right]

            if not level and next_level:
                level = next_level
                next_level = []

                if not left_to_right:
                    level_result = level_result[::-1]

                result.append(level_result)

                left_to_right = not left_to_right
                level_result = []

        return result



#------------------------------------------------------
# Solution 2 - iterative += replaced with append
#------------------------------------------------------

# Runtime:  18.64%
# Memory:   94.50%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        level = [root]
        next_level = []

        level_result = []
        left_to_right = True

        while level:
            node = level.pop(0)

            if node:
                level_result.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)

            if not level and next_level:
                level = next_level
                next_level = []

                if not left_to_right:
                    level_result = level_result[::-1]

                result.append(level_result)

                left_to_right = not left_to_right
                level_result = []

        return result



#------------------------------------------------------
# Solution 3 - iterative remove level_result reverse
#------------------------------------------------------

# Runtime:  76.15%
# Memory:   94.50%


 Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []

        level = [root]
        next_level = []

        level_result = []
        left_to_right = True

        while level:
            node = level.pop(0)

            if node:
                if left_to_right:
                    level_result.append(node.val)
                else:
                    level_result = [node.val] + level_result
                
                next_level += [node.left, node.right]

            if not level and next_level:
                level = next_level
                next_level = []

                result.append(level_result)

                left_to_right = not left_to_right
                level_result = []


        return result


#------------------------------------------------------
# Solution 4 - iterative short var names
#------------------------------------------------------

# Runtime:  24.41%
# Memory:   48.21%



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        r = []

        l = [root]
        nl = []

        lr = []
        ltr = True

        while l:
            n = l.pop(0)

            if n:
                if ltr:
                    lr.append(n.val)
                else:
                    lr = [n.val] + lr
                
                nl += [n.left, n.right]

            if not l and nl:
                l = nl
                nl = []

                r.append(lr)

                ltr = not ltr
                lr = []


        return r



#------------------------------------------------------
# Solution 5 - iterative replace all appends with +=
#------------------------------------------------------

# Runtime:  91.29%
# Memory:   94.50%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        r = []

        l = [root]
        nl = []

        lr = []
        ltr = True

        while l:
            n = l.pop(0)

            if n:
                if ltr:
                    lr += [n.val]
                else:
                    lr = [n.val] + lr
                
                nl += [n.left, n.right]

            if not l and nl:
                l = nl
                nl = []

                r += [lr]

                ltr = not ltr
                lr = []


        return r
