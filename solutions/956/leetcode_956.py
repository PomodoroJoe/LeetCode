#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        result = 0

        def tallestBillboardRecurse(index, left, right):
            nonlocal result

            if index >= len(rods):
                return

            rod = rods[index]

            new_left = left + rod
            new_right = right + rod

            if new_left == right:
                result = max(result, right)

            if new_right == left:
                result = max(result, left)

            tallestBillboardRecurse(index + 1, left, right)
            tallestBillboardRecurse(index + 1, new_left, right)
            tallestBillboardRecurse(index + 1, left, new_right)

        tallestBillboardRecurse(0, 0, 0)
        return result


#------------------------------------------------------
# Solution 2 - dynamic programming
#------------------------------------------------------

# Runtime:  73.68%
# Memory:   68.42%


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        # key = difference between the tall pole and the short pole
        # value = tall pole height
        dp = {0: 0}

        for rod in rods:
            new_dp = dp.copy()

            for key in dp:
                delta = key

                taller = dp[key]
                shorter = taller - delta

                new_taller = taller + rod
                new_taller_delta = new_taller - shorter

                new_shorter = shorter + rod #<-- might be taller than "taller"
                new_shorter_delta = abs(new_shorter - taller)

                new_dp[new_taller_delta] = max(new_taller, new_dp.get(new_taller_delta, 0))
                new_dp[new_shorter_delta] = max(new_shorter, taller, new_dp.get(new_shorter_delta, 0))

            dp = new_dp

        return dp[0]