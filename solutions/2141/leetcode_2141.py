#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  98.80%
# Memory:   49.40%


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        if len(batteries) < n:
            return 0

        sorted_batteries = sorted(batteries)

        if len(batteries) == n:
            return sorted_batteries[0]

        extra_battery_capacity = sum(sorted_batteries[:-n])

        start_index = len(batteries) - n
        target_index = start_index + 1

        current_capacity = sorted_batteries[start_index]

        while extra_battery_capacity > 0 and target_index < len(batteries):
            target_capacity = sorted_batteries[target_index]
            current_capacity_battery_count = target_index - start_index

            delta = target_capacity - current_capacity
            total_delta = (delta * current_capacity_battery_count)

            if extra_battery_capacity <= total_delta:
                return current_capacity + (extra_battery_capacity // current_capacity_battery_count)

            extra_battery_capacity -= total_delta
            current_capacity = target_capacity

            target_index += 1

        return current_capacity + (extra_battery_capacity // n)