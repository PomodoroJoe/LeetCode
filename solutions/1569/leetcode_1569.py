#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  97.67%
# Memory:   53.49%


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        result = 0

        def numWaysRecurse(tree):
            if len(tree) < 3:
                return 1

            root = tree[0]
            left_tree = [n for n in tree if n < root]
            right_tree = [n for n in tree if n > root]

            n = len(tree) - 1
            k = len(right_tree)

            left_op = numWaysRecurse(left_tree)
            right_op = numWaysRecurse(right_tree)

            return left_op * right_op * comb(n, k)

        result = numWaysRecurse(nums)
        return result % (pow(10, 9) + 7) - 1



#------------------------------------------------------
# Solution 2 - Solution 1 w/ k = len(left_tree)
#              (demonstrating no difference)
#------------------------------------------------------

# Runtime:  95.35%
# Memory:   53.49%


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        result = 0

        def numWaysRecurse(tree):
            if len(tree) < 3:
                return 1

            root = tree[0]
            left_tree = [n for n in tree if n < root]
            right_tree = [n for n in tree if n > root]

            n = len(tree) - 1
            k = len(left_tree)

            left_op = numWaysRecurse(left_tree)
            right_op = numWaysRecurse(right_tree)

            return left_op * right_op * comb(n, k)

        result = numWaysRecurse(nums)
        return result % (pow(10, 9) + 7) - 1