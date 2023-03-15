#------------------------------------------------------
# Solution 1 - level traversal to flatten tree w/ debug
#------------------------------------------------------

# Runtime:  23.49%
# Memory:   18.83%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        tree = [root]

        level = [root]
        next_level = []

        while level:
            node = level.pop(0)

            if node:
                next_level += [node.left, node.right]

            if level == []:
                tree += next_level

                level = next_level
                next_level = []

        nodes = [node.val if node else None for node in tree]
        print(nodes)

        prev_node = root
        for node in tree[1:]:
            if prev_node == None and node != None:
                return False
            prev_node = node
            
        return True



#------------------------------------------------------
# Solution 2 - level traversal to flatten tree
#------------------------------------------------------

# Runtime:  64.94%
# Memory:   96.89%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        tree = [root]

        level = [root]
        next_level = []

        while level:
            node = level.pop(0)

            if node:
                next_level += [node.left, node.right]

            if level == []:
                tree += next_level

                level = next_level
                next_level = []

        prev_node = root
        for node in tree[1:]:
            if prev_node == None and node != None:
                return False
            prev_node = node
            
        return True



#------------------------------------------------------
# Solution 3 - level traversal to flatten tree (better)
#------------------------------------------------------

# Runtime:  94.47%
# Memory:   61.14%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        tree = [root]

        level = [root]
        next_level = []

        while level:
            node = level.pop(0)

            if node:
                next_level += [node.left, node.right]

            if level == []:
                tree += next_level

                level = next_level
                next_level = []

        for i in range(1, len(tree)):
            if tree[i - 1] == None and tree[i] != None:
                return False
            
        return True

