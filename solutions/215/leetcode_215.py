#------------------------------------------------------
# Solution 1 - max heap
#------------------------------------------------------

# Runtime:  91.80%
# Memory:   32.28%


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-n for n in nums]
        heapq.heapify(heap)

        result = None
        for i in range(k):
            result = heapq.heappop(heap)

        return -result



#------------------------------------------------------
# Solution 2 - counts between min/max
#------------------------------------------------------

# Runtime:  99.63%
# Memory:   89.91%


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_val = min(nums)
        max_val = max(nums)

        counts = [0] * (max_val - min_val + 1)
        for n in nums:
            index = n - min_val
            counts[index] += 1

        index = len(counts) - 1
        remaining_k = k

        while index >= 0 and remaining_k > 0:
            count = counts[index]
            remaining_k -= count
            index -= 1

        return index + min_val + 1