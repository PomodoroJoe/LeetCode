#------------------------------------------------------
# Solution 1 - sorted array w/ prev element
#------------------------------------------------------

# Runtime:  61.33%
# Memory:   20.83%


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)

        delta = sorted_arr[1] - sorted_arr[0]

        prev_e = sorted_arr[1]
        for e in sorted_arr[2:]:
            if e - prev_e != delta:
                return False
            prev_e = e

        return True



#------------------------------------------------------
# Solution 2 - sorted array w/o prev element
#------------------------------------------------------

# Runtime:  39.71%
# Memory:   20.83%


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)

        delta = sorted_arr[1] - sorted_arr[0]

        for i in range(2, len(sorted_arr)):
            if sorted_arr[i] - sorted_arr[i - 1] != delta:
                return False

        return True