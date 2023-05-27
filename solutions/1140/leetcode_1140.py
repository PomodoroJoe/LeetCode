#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        max_index = len(piles) - 1

        def stoneGameRecurse(index, M, remaining_stones):
            result = 0

            if index > max_index:
                return 0

            min_X = 1
            max_X = 2 * M

            stones = 0

            for X in range(min_X, max_X + 1):
                current_index = index + X - 1
                if current_index > max_index:
                    continue

                stones += piles[current_index]

                next_index = current_index + 1
                next_M = max(M, X)
                next_remaining_stones = remaining_stones - stones

                bobs_score = stoneGameRecurse(next_index, next_M, next_remaining_stones)
                alices_score = remaining_stones - bobs_score

                result = max(result, alices_score)

            return result

        return stoneGameRecurse(0, 1, sum(piles))



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  58.49%
# Memory:   28.30%


from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        max_index = len(piles) - 1

        @cache
        def stoneGameRecurse(index, M, remaining_stones):
            result = 0

            if index > max_index:
                return 0

            min_X = 1
            max_X = 2 * M

            stones = 0

            for X in range(min_X, max_X + 1):
                current_index = index + X - 1
                if current_index > max_index:
                    continue

                stones += piles[current_index]

                next_index = current_index + 1
                next_M = max(M, X)
                next_remaining_stones = remaining_stones - stones

                bobs_score = stoneGameRecurse(next_index, next_M, next_remaining_stones)
                alices_score = remaining_stones - bobs_score

                result = max(result, alices_score)

            return result

        return stoneGameRecurse(0, 1, sum(piles))



#------------------------------------------------------
# Solution 7 - Solution 2 w/ optimizations
#------------------------------------------------------

# Runtime:  68.40%
# Memory:   25.47%


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        max_index = len(piles) - 1

        @cache
        def stoneGameRecurse(index, M, remaining_stones):
            result = 0

            if index > max_index:
                return 0

            max_X = 2 * M
            stones = 0

            for X in range(1, max_X + 1):
                current_index = index + X - 1
                if current_index > max_index:
                    return result

                stones += piles[current_index]
                next_M = M if M > X else X

                op = remaining_stones - stoneGameRecurse(current_index + 1, next_M, remaining_stones - stones)
                result = result if result > op else op

            return result

        return stoneGameRecurse(0, 1, sum(piles))