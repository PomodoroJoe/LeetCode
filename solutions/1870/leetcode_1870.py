#------------------------------------------------------
# Solution 1 - binary search
#------------------------------------------------------

# Runtime:  47.86%
# Memory:   25.64%


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        departure_count = ceil(hour)

        if departure_count < len(dist):
            return -1

        max_index = len(dist) - 1

        def is_valid_speed(speed):
            total_time = 0

            for i in range(len(dist)):
                time = dist[i] / speed
                total_time += ceil(time) if i != max_index else time

            return total_time <= hour

        slow = 1
        fast = 10 ** 7

        while slow < fast:
            mid = slow + ((fast - slow) // 2)

            if is_valid_speed(mid):
                fast = mid
            else:
                slow = mid + 1

        return slow