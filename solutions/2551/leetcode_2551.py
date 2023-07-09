#------------------------------------------------------
# Solution 1 - split points
#------------------------------------------------------

# Runtime:  78.18%
# Memory:   44.55%


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        split_points = []

        for index in range(len(weights) - 1):
            split_cost = weights[index] + weights[index + 1]
            split_points.append(split_cost)

        sorted_split_points = sorted(split_points)
        min_score = sum(sorted_split_points[:(k - 1)])

        max_score = sum(sorted_split_points[(len(weights) - k ):])

        return max_score - min_score