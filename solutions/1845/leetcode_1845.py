#------------------------------------------------------
# Solution 1 - heap (pre-populated)
#------------------------------------------------------

# Runtime:  27.48%
# Memory:   67.29%


class SeatManager:

    def __init__(self, n: int):
        self.heap = [x for x in range(1, n + 1)]
        heapq.heapify(self.heap)


    def reserve(self) -> int:
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)



#------------------------------------------------------
# Solution 2 - heap
#------------------------------------------------------

# Runtime:  96.11%
# Memory:   98.79%


class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.next_seat = 0


    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.next_seat += 1
        return self.next_seat
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)