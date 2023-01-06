#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime: 41.36%
# Memory:  17.54%

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)

        remaining_coins = coins
        result = 0

        for cost in sorted_costs:
            if cost <= remaining_coins:
                remaining_coins -= cost
                result += 1
            else:
                break

        return result




#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# sort in-place (not recommended!)

# Runtime: 90.50%
# Memory:  61.26%

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        remaining_coins = coins
        result = 0

        for cost in costs:
            if cost <= remaining_coins:
                remaining_coins -= cost
                result += 1
            else:
                break

        return result
