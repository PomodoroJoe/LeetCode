#------------------------------------------------------
# Solution 1 - two pass
#------------------------------------------------------

# Runtime:  83.85%
# Memory:   99.34%


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_for_kid = [1] * len(ratings)
        max_index = len(ratings) - 1

        # pass 1 - left to right
        for i in range(1, max_index + 1):
            if ratings[i] > ratings[i - 1]:
                candy_for_kid[i] = candy_for_kid[i - 1] + 1

        # pass 2 - right to left
        for i in range(max_index - 1, -1, -1):
            if ratings[i] > ratings[i + 1] and candy_for_kid[i] <= candy_for_kid[i + 1]:
                candy_for_kid[i] = candy_for_kid[i + 1] + 1

        return sum(candy_for_kid)