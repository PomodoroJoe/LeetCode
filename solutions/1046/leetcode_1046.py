#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  45.14%
# Memory:   47.46%


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]

        sorted_stones = sorted(stones)

        if sorted_stones[-1] == sorted_stones[-2]:
            new_sorted_stones = sorted_stones[:-2]

            return self.lastStoneWeight(new_sorted_stones)

        new_stone_weight = sorted_stones[-1] - sorted_stones[-2]
        new_sorted_stones = sorted_stones[:-2] + [new_stone_weight]

        return self.lastStoneWeight(new_sorted_stones)



#------------------------------------------------------
# Solution 5 - recursive (compact)
#------------------------------------------------------

# Runtime:  70.88%
# Memory:   47.46%


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        if len(stones) == 1:
            return stones[0]

        sorted_stones = sorted(stones)

        if sorted_stones[-1] != sorted_stones[-2]:
            sorted_stones = sorted_stones[:-2] + [sorted_stones[-1] - sorted_stones[-2]]
            return self.lastStoneWeight(sorted_stones)

        return self.lastStoneWeight(sorted_stones[:-2])