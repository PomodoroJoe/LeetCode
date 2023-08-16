#------------------------------------------------------
# Solution 1 - max()
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        left = 0
        right = k

        while right <= len(nums):
            max_value = max(nums[left:right])
            result.append(max_value)

            left += 1
            right += 1

        return result



#------------------------------------------------------
# Solution 2 - heap
#------------------------------------------------------

# Runtime:  58.53%
# Memory:    5.24%


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        left = 0
        right = k

        # (-val, index)
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))

        result.append(-heap[0][0])

        while right < len(nums):
            left += 1

            while heap and heap[0][1] < left:
                heapq.heappop(heap)

            heapq.heappush(heap, (-nums[right], right))

            result.append(-heap[0][0])
            right += 1

        return result


#------------------------------------------------------
# Solution 3 - queue
#------------------------------------------------------

# Runtime:  76.51%
# Memory:   70.42%


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        left = 0
        right = k

        # index of max value at 0, all potential future max values
        queue = [0]

        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i)

        result.append(nums[queue[0]])

        while right < len(nums):
            if queue and queue[0] <= left:
                queue.pop(0)

            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop(-1)
            queue.append(right)

            result.append(nums[queue[0]])

            left += 1
            right += 1

        return result


#------------------------------------------------------
# Solution 4 - Solution 3 w/ deque
#------------------------------------------------------

# Runtime:  95.61%
# Memory:   21.40%


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        
        left = 0
        right = k

        # index of max value at 0, all potential future max values
        queue = deque([0])

        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

        result.append(nums[queue[0]])

        while right < len(nums):
            if queue and queue[0] <= left:
                queue.popleft()

            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            result.append(nums[queue[0]])

            left += 1
            right += 1

        return result