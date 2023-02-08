#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  98.53%
# Memory:   54.98%


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        result = 0

        pos = 0
        max_jump = pos + nums[pos]
        best_jump = 0

        while max_jump < len(nums) - 1:
            for i in range(pos, max_jump + 1):
                if i + nums[i] > best_jump + nums[best_jump]:
                    best_jump = i

            pos = best_jump
            result += 1
            max_jump = pos + nums[pos]

        return result + 1