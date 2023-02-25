#------------------------------------------------------
# Solution 1 - min/max
#------------------------------------------------------

# Runtime:  55.13%
# Memory:   82.91%


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        low = prices[0]
        high = low

        for price in prices:
            low = min(low, price)
            result = max(result, price - low)

        return result



#------------------------------------------------------
# Solution 2 - if
#------------------------------------------------------

# Runtime:  99.12%
# Memory:   82.91%


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        low = prices[0]

        for price in prices:
            if price < low:
                low = price
            
            profit = price - low

            if profit > result:
                result = profit

        return result
