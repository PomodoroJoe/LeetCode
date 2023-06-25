#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mod_val = (10 ** 9) + 7

        def countRoutesRecurse(start_city, remaining_fuel):
            result = 0

            if remaining_fuel < 0:
                return 0

            if start_city == finish:
                result = 1

            start_location = locations[start_city]

            for end_city, location in enumerate(locations):
                if end_city == start_city:
                    continue

                new_remaining_fuel = remaining_fuel - abs(start_location - location)
                result += countRoutesRecurse(end_city, new_remaining_fuel)

            return result % mod_val

        result = countRoutesRecurse(start, fuel)
        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  71.63%
# Memory:   17.20%


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mod_val = (10 ** 9) + 7

        @cache
        def countRoutesRecurse(start_city, remaining_fuel):
            result = 0

            if remaining_fuel < 0:
                return 0

            if start_city == finish:
                result = 1

            start_location = locations[start_city]

            for end_city, location in enumerate(locations):
                if end_city == start_city:
                    continue

                new_remaining_fuel = remaining_fuel - abs(start_location - location)
                result += countRoutesRecurse(end_city, new_remaining_fuel)

            return result % mod_val

        result = countRoutesRecurse(start, fuel)
        return result


#------------------------------------------------------
# Solution 3 - Solution 1 w/ dynamic programming
#------------------------------------------------------

# Runtime:  23.41%
# Memory:   20.57%


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mod_val = (10 ** 9) + 7

        dp = {}
        
        def countRoutesRecurse(start_city, remaining_fuel):
            key = (start_city, remaining_fuel)
            if key in dp:
                return dp[key]

            result = 0

            if remaining_fuel < 0:
                dp[key] = 0
                return 0

            if start_city == finish:
                result = 1

            start_location = locations[start_city]

            for end_city, location in enumerate(locations):
                if end_city == start_city:
                    continue

                new_remaining_fuel = remaining_fuel - abs(start_location - location)
                result += countRoutesRecurse(end_city, new_remaining_fuel)

            dp[key] = result % mod_val
            return dp[key]

        result = countRoutesRecurse(start, fuel)
        return result