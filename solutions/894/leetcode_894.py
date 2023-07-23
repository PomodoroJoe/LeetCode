#------------------------------------------------------
# Solution 1 - dynamic programming
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   80.50%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        # index = node_count, value = list of all trees with node_count
        dp = [None for _ in range(n + 1)]
        dp[1] = [TreeNode()]

        for i in range(2, n + 1):
            tree_list = []

            remaining_nodes = i - 1

            for j in range(1, remaining_nodes + 1):
                left_options = dp[j]
                right_options = dp[remaining_nodes - j]

                if left_options == None or right_options == None:
                    continue

                for left in left_options:
                    for right in right_options:
                        root_node = TreeNode(0, left, right)
                        tree_list.append(root_node)

                if not tree_list:
                    dp[i] = None
                else:
                    dp[i] = tree_list 
        
        result = dp[n]
        return result