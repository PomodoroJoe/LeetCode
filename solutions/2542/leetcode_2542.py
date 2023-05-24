#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_index = len(nums1) - 1

        def maxScoreRecurse(index, total, min_m, remaining_k):
            if remaining_k == 0:
                return total * min_m

            if index > max_index:
                return 0

            op1 = maxScoreRecurse(index + 1, total, min_m, remaining_k)
            
            op2 = 0
            new_total = total + nums1[index]
            new_min_m = min(min_m, nums2[index])
            op2 = maxScoreRecurse(index + 1, new_total, new_min_m, remaining_k - 1)

            return max(op1, op2)

        return maxScoreRecurse(0, 0, inf, k)



#------------------------------------------------------
# Solution 2 - sorting & min heap
#------------------------------------------------------

# Runtime:  91.22%
# Memory:   23.28%


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        elements = []

        for i in range(len(nums1)):
            e = (nums1[i], nums2[i])
            elements.append(e)

        # sort by multiplier
        elements.sort(key=lambda x: x[1], reverse = True)

        result = 0
        total = 0
        min_m = inf
        heap = []

        for i in range(k):
            val, m = elements[i]
            heapq.heappush(heap, val)
            total += val
            min_m = m

        result = total * min_m

        for i in range(k, len(elements)):
            val, m = elements[i]
            if val > heap[0]:
                removed = heapq.heappop(heap)
                total -= removed
                total += val

                heapq.heappush(heap, val)
                result = max(result, total * m)

        return result