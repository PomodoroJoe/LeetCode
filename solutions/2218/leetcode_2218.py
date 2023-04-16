#------------------------------------------------------
# Solution 1 - simple recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   1N/A


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        result = 0

        if k == 0:
            return 0

        for pile_index in range(len(piles)):
            if not piles[pile_index]:
                continue

            coin = piles[pile_index].pop(0)

            option = coin + self.maxValueOfCoins(piles, k - 1)
            result = max(result, option)

            piles[pile_index] = [coin] + piles[pile_index]

        return result




#------------------------------------------------------
# Solution 2 - recursive with pile_index
#------------------------------------------------------


# Runtime:  54.40%
# Memory:   16.77%


from functools import cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        @cache
        def maxValueOfCoinsRecurse(pile_index, remaining_k):
            if remaining_k == 0:
                return 0

            if pile_index >= len(piles):
                return 0

            pile = piles[pile_index]

            coins_count = len(pile)
            max_coins = min(remaining_k, coins_count)

            result = maxValueOfCoinsRecurse(pile_index + 1, remaining_k)

            total = 0
            for i in range(max_coins):
                total += pile[i]

                coins_taken = i + 1
                new_remaining_k = remaining_k - coins_taken

                option = total + maxValueOfCoinsRecurse(pile_index + 1, new_remaining_k)

                result = max(result, option)

            return result

        return maxValueOfCoinsRecurse(0, k)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ cached len & custom min/max
#------------------------------------------------------


# Runtime:  96.89%
# Memory:    6.21%


from functools import cache

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        pile_count = len(piles)
        pile_lengths = [len(pile) for pile in piles]

        @cache
        def maxValueOfCoinsRecurse(pile_index, remaining_k):
            if remaining_k == 0:
                return 0

            if pile_index >= pile_count:
                return 0

            pile = piles[pile_index]

            coins_count = pile_lengths[pile_index]
            max_coins = remaining_k if remaining_k < coins_count else coins_count

            result = maxValueOfCoinsRecurse(pile_index + 1, remaining_k)

            total = 0
            for i in range(max_coins):
                total += pile[i]

                coins_taken = i + 1
                new_remaining_k = remaining_k - coins_taken

                option = total + maxValueOfCoinsRecurse(pile_index + 1, new_remaining_k)

                result = result if result > option else option

            return result

        return maxValueOfCoinsRecurse(0, k)