
#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)

        if len(weights) <= days:
            return max(weights)

        result = sum(weights)

        total_weight = 0
        for i in range(len(weights) - 1):
            total_weight += weights[i]
            remaining = self.shipWithinDays(weights[i+1:], days - 1)

            option = max(total_weight, remaining)
            result = min(result, option)

        return result



#------------------------------------------------------
# Solution 2 - linear search
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)

        result = min_weight

        def AcceptableWeightLimit(limit):
            day_count = 1
            day_weight = 0

            for weight in weights:
                day_weight += weight
                if day_weight > limit:
                    day_count += 1
                    day_weight = weight

            return day_count <= days

        while not AcceptableWeightLimit(result):
            result += 1

        return result



#------------------------------------------------------
# Solution 3 - binary search
#------------------------------------------------------

# Runtime:  23.46%
# Memory:   97.85%



class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)

        def AcceptableWeightLimit(limit):
            day_count = 1
            day_weight = 0

            for weight in weights:
                day_weight += weight
                if day_weight > limit:
                    day_count += 1
                    if day_count > days:
                        return False
                    day_weight = weight

            return True


        lower = min_weight
        upper = max_weight

        while lower < upper:
            mid = lower + ((upper - lower) // 2)

            if AcceptableWeightLimit(mid):
                upper = mid
            else:
                lower = mid + 1

        return lower



#------------------------------------------------------
# Solution 4 - binary search w/ better upper bound
#------------------------------------------------------

# Runtime:  98.62%
# Memory:   78.60%

# max_weight:  ceiling (number of packages / days) to get the
#              number of packages needed to ship per day, then
#              multiply that by the heaviest single package
#              to get an upper bound for a single day's weight.


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = ceil(len(weights) / days) * min_weight

        def AcceptableWeightLimit(limit):
            day_count = 1
            day_weight = 0

            for weight in weights:
                day_weight += weight
                if day_weight > limit:
                    day_count += 1
                    if day_count > days:
                        return False
                    day_weight = weight

            return True


        lower = min_weight
        upper = max_weight

        while lower < upper:
            mid = lower + ((upper - lower) // 2)

            if AcceptableWeightLimit(mid):
                upper = mid
            else:
                lower = mid + 1

        return lower
