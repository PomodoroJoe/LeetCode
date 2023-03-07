#------------------------------------------------------
# Solution 1 - linear brute force
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def tripsWithTime(T):
            trips = 0
            for bus in time:
                trips += T // bus
            return trips

        result = 1

        while tripsWithTime(result) < totalTrips:
            result += 1

        return result



#------------------------------------------------------
# Solution 2 - binary search with linear search finish
#------------------------------------------------------

# Runtime:  35.25%
# Memory:   20.50%


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def tripsWithTime(T):
            trips = 0
            for bus in time:
                trips += T // bus
            return trips

        lower_bound = min(time)
        upper_bound = max(time) * totalTrips

        while upper_bound >= lower_bound:
            mid = lower_bound + ((upper_bound - lower_bound) // 2)

            trips = tripsWithTime(mid)

            if trips < totalTrips:
                lower_bound = mid + 1
            elif trips > totalTrips:
                upper_bound = mid - 1
            else:
                while tripsWithTime(mid) == totalTrips:
                    mid -= 1
                return mid + 1

        return lower_bound




#------------------------------------------------------
# Solution 3 - binary search
#------------------------------------------------------

# Runtime:  35.25%
# Memory:   20.50%


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def tripsWithTime(T):
            trips = 0
            for bus in time:
                trips += T // bus
            return trips

        result = 0

        lower_bound = min(time)
        upper_bound = max(time) * totalTrips

        while upper_bound >= lower_bound:
            mid = lower_bound + ((upper_bound - lower_bound) // 2)

            trips = tripsWithTime(mid)

            if trips < totalTrips:
                lower_bound = mid + 1
            else:
                result = mid
                upper_bound = mid - 1

        return result



#------------------------------------------------------
# Solution 3 - binary search with better bounds
#------------------------------------------------------

# Runtime:  89.25%
# Memory:   20.50%


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        result = 0

        lower_bound = min(time)
        upper_bound = lower_bound * totalTrips

        while upper_bound >= lower_bound:
            mid = (lower_bound + upper_bound) // 2

            trips = 0
            for bus in time:
                trips += mid // bus

            if trips < totalTrips:
                lower_bound = mid + 1
            else:
                result = mid
                upper_bound = mid - 1

        return result