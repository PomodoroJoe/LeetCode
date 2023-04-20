#------------------------------------------------------
# Solution 1 - level order traversal
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        def score(current_level):
            start_node_index = None
            end_node_index = None

            for index in range(len(current_level)):
                if current_level[index]:
                    if start_node_index == None:
                        start_node_index = index
                    end_node_index = index

            return (end_node_index - start_node_index) + 1 if start_node_index != None else 0


        result = 1

        level = [root]
        next_level = []

        while level:
            node = level.pop(0)

            if node:
                next_level.append(node.left)
                next_level.append(node.right)
            else:
                if next_level:
                    next_level.append(None)
                    next_level.append(None)

            if not level and next_level:
                level = next_level
                next_level = []

                level_score = score(level)
                result = max(result, level_score)

        return result



#------------------------------------------------------
# Solution 2 - level order traversal w/ (node, index)
#------------------------------------------------------

# Runtime:  40.73%
# Memory:   39.00%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        def score(current_level):
            if not current_level:
                return 0

            start_node_index = current_level[0][1]
            end_node_index = current_level[-1][1]

            return (end_node_index - start_node_index) + 1 if start_node_index != None else 0


        result = 1

        level = [(root, 0)]
        next_level = []

        while level:
            node, index = level.pop(0)

            if node:
                next_index = index * 2
                if node.left:
                    next_level.append((node.left, next_index))
                if node.right:
                    next_level.append((node.right, next_index + 1))

            if not level and next_level:
                level = next_level
                next_level = []

                level_score = score(level)
                result = max(result, level_score)

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 w/o score function
#------------------------------------------------------

# Runtime:  54.74%
# Memory:   67.85%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1

        level = [(root, 0)]
        next_level = []

        while level:
            node, index = level.pop(0)

            if node:
                next_index = index * 2
                if node.left:
                    next_level.append((node.left, next_index))
                if node.right:
                    next_level.append((node.right, next_index + 1))

            if not level and next_level:
                level = next_level
                next_level = []

                start_node_index = level[0][1]
                end_node_index = level[-1][1]
                level_score = (end_node_index - start_node_index) + 1 if start_node_index != None else 0
                
                result = result if result > level_score else level_score

        return result




#------------------------------------------------------
# Solution 4 - Solution 3 w/ for loop
#------------------------------------------------------

# Runtime:  81.40%
# Memory:   39.00%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1

        level = [(root, 0)]
        next_level = []

        while level:
            for node, index in level:
                if node:
                    next_index = index * 2
                    if node.left:
                        next_level.append((node.left, next_index))
                    if node.right:
                        next_level.append((node.right, next_index + 1))
            
            level = []
            if next_level:
                level = next_level
                next_level = []

                start_node_index = level[0][1]
                end_node_index = level[-1][1]
                level_score = (end_node_index - start_node_index) + 1 if start_node_index != None else 0
                
                result = result if result > level_score else level_score

        return result



#------------------------------------------------------
# Solution 6 - Solution 4 w/o unnecessary if/else
#------------------------------------------------------

# Runtime:  93.74%
# Memory:   95.17%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1

        level = [(root, 0)]
        next_level = []

        while level:
            for node, index in level:
                if node:
                    next_index = index * 2
                    if node.left:
                        next_level.append((node.left, next_index))
                    if node.right:
                        next_level.append((node.right, next_index + 1))
            
            level = []
            if next_level:
                level = next_level
                next_level = []

                start_node_index = level[0][1]
                end_node_index = level[-1][1]
                level_score = (end_node_index - start_node_index) + 1
                
                result = result if result > level_score else level_score

        return result