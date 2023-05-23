#------------------------------------------------------
# Solution 1 - sort
#------------------------------------------------------

# Runtime:   6.15%
# Memory:    6.32%


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_index = k - 1
        self.stream = nums.copy()
        

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse = True)
        return self.stream[self.k_index]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



#------------------------------------------------------
# Solution 2 - heap
#------------------------------------------------------

# Runtime:  98.22%
# Memory:   17.70%


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums.copy()
        heapq.heapify(self.stream)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

        return self.stream[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)