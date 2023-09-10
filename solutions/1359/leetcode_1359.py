#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:   5.11%
# Memory:    5.53%


class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = ((10 ** 9) + 7)

        @cache
        def countOrdersRecurse(pickups, deliveries):
            if deliveries == 0:
                return 1

            option1 = 0
            if pickups > 0:
                option1 = pickups * countOrdersRecurse(pickups - 1, deliveries)

            option2 = 0
            if pickups < deliveries:
                option2 = (deliveries - pickups) * countOrdersRecurse(pickups, deliveries - 1)

            return (option1 + option2) % mod

        return countOrdersRecurse(n, n) % mod



#------------------------------------------------------
# Solution 2 - Solution 1 w/ running mod
#------------------------------------------------------

# Runtime:  11.91%
# Memory:    7.23%


class Solution:
    def countOrders(self, n: int) -> int:
        
        mod = ((10 ** 9) + 7)

        @cache
        def countOrdersRecurse(pickups, deliveries):
            if deliveries == 0:
                return 1

            option1 = 0
            if pickups > 0:
                option1 = pickups * countOrdersRecurse(pickups - 1, deliveries)

            option2 = 0
            if pickups < deliveries:
                option2 = (deliveries - pickups) * countOrdersRecurse(pickups, deliveries - 1)

            return (option1 + option2) % mod

        return countOrdersRecurse(n, n) % mod