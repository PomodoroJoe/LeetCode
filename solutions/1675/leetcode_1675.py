#------------------------------------------------------
# Solution 1 - sorted list
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        result = sorted_nums[-1] - sorted_nums[0]

        # LOW |-----> <-----| HIGH
        # ODD |-----> x2
        #         //2 <-----| EVEN

        # LOW ----->
        while sorted_nums[0] % 2 == 1:
            sorted_nums[0] *= 2
            sorted_nums.sort()  #<-- red flag

            result = min(result, sorted_nums[-1] - sorted_nums[0])

        # <----- HIGH
        while sorted_nums[-1] % 2 == 0:
            sorted_nums[-1] = sorted_nums[-1] // 2
            sorted_nums.sort()

            result = min(result, sorted_nums[-1] - sorted_nums[0])

        return result



#------------------------------------------------------
# Solution 2 - heaps
#------------------------------------------------------

# Runtime:  43.48%
# Memory:   65.22%


import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        result = sorted_nums[-1] - sorted_nums[0]

        # LOW |-----> <-----| HIGH
        # ODD |-----> x2
        #         //2 <-----| EVEN

        min_heap = sorted_nums
        heapq.heapify(min_heap)
        
        max_num = sorted_nums[-1]

        # LOW ----->
        while min_heap[0] % 2 == 1:
            #sorted_nums[0] *= 2
            min_num = heappop(min_heap)
            min_num *= 2

            max_num = max(max_num, min_num)

            #sorted_nums.sort()  #<-- red flag
            heapq.heappush(min_heap, min_num)

            result = min(result, max_num - min_heap[0])



        def max_heappush(heap, item):
            heapq.heappush(heap, -item)

        def max_heappop(heap):
            return -heapq.heappop(heap)

        def max_heappeek(heap):
            return -heap[0]

        max_heap = [-x for x in min_heap]
        heapq.heapify(max_heap)

        min_num = min_heap[0]

        # <----- HIGH
        while max_heappeek(max_heap) % 2 == 0:
            #sorted_nums[-1] = sorted_nums[-1] // 2
            max_num = max_heappop(max_heap)
            max_num = max_num // 2

            min_num = min(min_num, max_num)

            #sorted_nums.sort()
            max_heappush(max_heap, max_num)

            result = min(result, max_heappeek(max_heap) - min_num)

        return result



#------------------------------------------------------
# Solution 3 - heaps w/ reduced input (BEST!)
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   33.33%


import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sorted_nums = sorted(list(nums_set))

        result = sorted_nums[-1] - sorted_nums[0]

        # LOW |-----> <-----| HIGH
        # ODD |-----> x2
        #         //2 <-----| EVEN

        min_heap = sorted_nums
        heapq.heapify(min_heap)

        max_num = sorted_nums[-1]

        # LOW ----->
        while min_heap[0] % 2 == 1:
            #sorted_nums[0] *= 2
            min_num = heappop(min_heap)
            min_num *= 2

            max_num = max(max_num, min_num)

            #sorted_nums.sort()  #<-- red flag
            heapq.heappush(min_heap, min_num)

            result = min(result, max_num - min_heap[0])



        def max_heappush(heap, item):
            heapq.heappush(heap, -item)

        def max_heappop(heap):
            return -heapq.heappop(heap)

        def max_heappeek(heap):
            return -heap[0]

        max_heap = [-x for x in min_heap]
        heapq.heapify(max_heap)

        min_num = min_heap[0]

        # <----- HIGH
        while max_heappeek(max_heap) % 2 == 0:
            #sorted_nums[-1] = sorted_nums[-1] // 2
            max_num = max_heappop(max_heap)
            max_num = max_num // 2

            min_num = min(min_num, max_num)

            #sorted_nums.sort()
            max_heappush(max_heap, max_num)

            result = min(result, max_heappeek(max_heap) - min_num)

        return result