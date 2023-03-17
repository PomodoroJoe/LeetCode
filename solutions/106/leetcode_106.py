#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  30.14%
# Memory:   06.72%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if inorder == []:
            return None

        root_val = postorder[-1]
    
        inorder_root_index = inorder.index(root_val)

        left_inorder = inorder[:inorder_root_index]
        right_inorder = inorder[inorder_root_index + 1:]

        left_tree_size = len(left_inorder)

        left_postorder = postorder[:left_tree_size]
        right_postorder = postorder[left_tree_size:-1]

        root = TreeNode(val = root_val)
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root



#------------------------------------------------------
# Solution 2 - recursive w/ indexes
#------------------------------------------------------

# Runtime:  62.17%
# Memory:   64.82%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def buildTreeRecurse(inorder_start, inorder_end, postorder_start, postorder_end):
            if (inorder_end - inorder_start) < 0:
                return None

            root_val = postorder[postorder_end]
        
            inorder_root_index = inorder.index(root_val)

            # left_inorder = inorder[:inorder_root_index]
            left_inorder_start = inorder_start
            left_inorder_end = inorder_root_index - 1

            #right_inorder = inorder[inorder_root_index + 1:]
            right_inorder_start = inorder_root_index + 1
            right_inorder_end = inorder_end

            #left_tree_size = len(left_inorder)
            left_tree_size = (left_inorder_end - left_inorder_start) + 1

            #left_postorder = postorder[:left_tree_size]
            left_postorder_start = postorder_start
            left_postorder_end = postorder_start + left_tree_size - 1

            #right_postorder = postorder[left_tree_size:-1]
            right_postorder_start = postorder_start + left_tree_size
            right_postorder_end = postorder_end - 1

            root = TreeNode(val = root_val)
            root.left = buildTreeRecurse(left_inorder_start, left_inorder_end, left_postorder_start, left_postorder_end)
            root.right = buildTreeRecurse(right_inorder_start, right_inorder_end, right_postorder_start, right_postorder_end)

            return root
        return buildTreeRecurse(0, len(inorder) - 1, 0, len(postorder) - 1)