#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  87.18%
# Memory:   50.96%


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)

        max_candies = max(candies)

        for kid, candy_count in enumerate(candies):
            if candy_count + extraCandies >= max_candies:
                result[kid] = True

        return result



#------------------------------------------------------
# Solution 3 - Solution 1 w/ custom max()
#------------------------------------------------------

# Runtime:  98.48%
# Memory:   50.96%


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)

        max_candies = 0
        for candy in candies:
            max_candies = max_candies if max_candies > candy else candy

        for kid, candy_count in enumerate(candies):
            if candy_count + extraCandies >= max_candies:
                result[kid] = True

        return result