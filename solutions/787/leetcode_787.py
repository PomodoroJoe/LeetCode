#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        result = -1

        if src == dst:
            return 0

        if k < 0:
            return -1

        available_flights = []

        for index, flight in enumerate(flights):
            if flight[0] == src:
                available_flights.append(index)

        for flight_index in available_flights:
            flight = flights[flight_index]

            option = self.findCheapestPrice(n, flights, flight[1], dst, k - 1)
            if option == -1:
                continue

            total_cost = flight[2] + option
            result = min(result, total_cost) if result != -1 else total_cost

        return result
Console



#------------------------------------------------------
# Solution 2 - recursive w/ cache
#------------------------------------------------------

# Runtime:   5.20%
# Memory:   11.74%


from functools import cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        @cache
        def findCheapestPriceRecurse(src, dst, k):
            result = -1

            if src == dst:
                return 0

            if k < 0:
                return -1

            available_flights = []

            for index, flight in enumerate(flights):
                if flight[0] == src:
                    available_flights.append(index)

            for flight_index in available_flights:
                flight = flights[flight_index]

                option = findCheapestPriceRecurse(flight[1], dst, k - 1)
                if option == -1:
                    continue

                total_cost = flight[2] + option
                result = min(result, total_cost) if result != -1 else total_cost

            return result

        return findCheapestPriceRecurse(src, dst, k)
Console



#------------------------------------------------------
# Solution 1 - recursive w/ cache & data preprocessing
#------------------------------------------------------

# Runtime:  46.61%
# Memory:   11.74%


from functools import cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        flight_map = defaultdict(list)

        for index, flight in enumerate(flights):
            flight_map[flight[0]].append(index)

        @cache
        def findCheapestPriceRecurse(src, dst, k):
            result = -1

            if src == dst:
                return 0

            if k < 0:
                return -1

            available_flights = flight_map[src]

            for flight_index in available_flights:
                flight = flights[flight_index]

                option = findCheapestPriceRecurse(flight[1], dst, k - 1)
                if option == -1:
                    continue

                total_cost = flight[2] + option
                result = min(result, total_cost) if result != -1 else total_cost

            return result

        return findCheapestPriceRecurse(src, dst, k)
