#------------------------------------------------------
# Solution 1 - tuple fingerprint with node queue
#------------------------------------------------------

# Runtime:   5.20%
# Memory:    5.13%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        def fingerprintNode(node):
            if node == None:
                return None
            return (fingerprintNode(node.left), node.val, fingerprintNode(node.right))

        fingerprint_counts = defaultdict(int)

        queue = [root]

        while queue:
            node = queue.pop(0)

            if not node:
                continue

            node_fingerprint = fingerprintNode(node)
            fingerprint_counts[node_fingerprint] += 1

            if fingerprint_counts[node_fingerprint] == 2:
                result.append(node)

            queue.append(node.left)
            queue.append(node.right)

        return result



#------------------------------------------------------
# Solution 2 - tuple fingerprint with node queue & dp
#------------------------------------------------------

# Runtime:  12.26%
# Memory:   91.86%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        dp = {}

        def fingerprintNode(node):
            if node == None:
                return None

            if node in dp:
                return dp[node]

            dp[node] = (fingerprintNode(node.left), node.val, fingerprintNode(node.right))
            return dp[node]

        fingerprint_counts = defaultdict(int)

        queue = [root]

        while queue:
            node = queue.pop(0)

            if not node:
                continue

            node_fingerprint = fingerprintNode(node)
            fingerprint_counts[node_fingerprint] += 1

            if fingerprint_counts[node_fingerprint] == 2:
                result.append(node)

            queue.append(node.left)
            queue.append(node.right)

        return result




#------------------------------------------------------
# Solution 3 - tuple fingerprint DFS with dp
#------------------------------------------------------

# Runtime:  11.26%
# Memory:   99.55%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        dp = {}
        fingerprint_counts = defaultdict(int)

        def fingerprintNode(node):
            if node == None:
                return None

            if node in dp:
                fingerprint = dp[node]
                fingerprint_counts[fingerprint] += 1
                if fingerprint_counts[fingerprint] == 2:
                    result.append(node)

                return fingerprint

            fingerprint = (fingerprintNode(node.left), node.val, fingerprintNode(node.right))
            fingerprint_counts[fingerprint] += 1
            if fingerprint_counts[fingerprint] == 2:
                result.append(node)

            return fingerprint

        fingerprintNode(root)
        return result



#------------------------------------------------------
# Solution 4 - tuple fingerprint DFS w/ DP & helper func
#------------------------------------------------------

# Runtime:  12.26%
# Memory:  100.00%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        dp = {}
        fingerprint_counts = defaultdict(int)

        def registerFingerprint(node, fingerprint):
            fingerprint_counts[fingerprint] += 1
            if fingerprint_counts[fingerprint] == 2:
                result.append(node)

        def fingerprintNode(node):
            if node == None:
                return None

            if node in dp:
                fingerprint = dp[node]
                registerFingerprint(node, fingerprint)
                return fingerprint

            fingerprint = (fingerprintNode(node.left), node.val, fingerprintNode(node.right))
            registerFingerprint(node, fingerprint)
            return fingerprint

        fingerprintNode(root)
        return result



#------------------------------------------------------
# Solution 5 - string fingerprint w/ DFS, DP, helper func
#------------------------------------------------------

# Runtime:  91.30%
# Memory:   17.95%


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []

        dp = {}
        fingerprint_counts = defaultdict(int)

        def registerFingerprint(node, fingerprint):
            fingerprint_counts[fingerprint] += 1
            if fingerprint_counts[fingerprint] == 2:
                result.append(node)

        def fingerprintNode(node):
            if node == None:
                return None

            if node in dp:
                fingerprint = dp[node]
                registerFingerprint(node, fingerprint)
                return fingerprint

            fingerprint = "{}.{}.{}".format(node.val, fingerprintNode(node.left), fingerprintNode(node.right))
            registerFingerprint(node, fingerprint)
            return fingerprint

        fingerprintNode(root)
        return result