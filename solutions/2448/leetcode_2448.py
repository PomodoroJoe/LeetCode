#------------------------------------------------------
# Solution 1 - brute force (check all values)
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        result = inf

        n = len(nums)

        num_to_cost_map = defaultdict(int)
        
        for i in range(n):
            num = nums[i]
            num_to_cost_map[num] += cost[i]

        sorted_nums = sorted(num_to_cost_map.keys())

        for target_num in sorted_nums:
            total_cost = 0

            for num in sorted_nums:
                delta = abs(num - target_num)
                total_cost += num_to_cost_map[num] * delta

            result = min(result, total_cost)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 ignoring bad target values
#------------------------------------------------------

# Runtime:  98.57%
# Memory:   38.37%


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        result = inf

        n = len(nums)

        num_to_cost_map = defaultdict(int)
        
        for i in range(n):
            num = nums[i]
            num_to_cost_map[num] += cost[i]

        sorted_nums = sorted(num_to_cost_map.keys())

        total_cost = sum(cost)
        left_group_cost = 0
        right_group_cost = total_cost

        for target_num in sorted_nums:
            left_group_cost += num_to_cost_map[target_num]
            right_group_cost = total_cost - left_group_cost

            if left_group_cost < right_group_cost:
                continue

            result = 0
            for num in sorted_nums:
                delta = abs(num - target_num)
                result += num_to_cost_map[num] * delta

            return result

        return result