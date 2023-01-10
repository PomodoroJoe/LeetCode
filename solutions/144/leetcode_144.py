#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  68.31%
# Memory:   56.74%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        # preorder = Node -> Left -> Right
        result = []
        
        stack = [root]
        while stack:
            node = stack.pop(-1)

            if node == None:
                continue

            result.append(node.val)

            stack.append(node.right)
            stack.append(node.left)

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:  87.10%
# Memory:   96.71%

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        # preorder = Node -> Left -> Right
        result = []
        
        stack = [root]
        while stack:
            node = stack.pop(-1)

            if node == None:
                continue

            result.append(node.val)

            stack.append(node.right)
            stack.append(node.left)

        return result
