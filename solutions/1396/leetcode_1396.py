#------------------------------------------------------
# Solution 1 - dictionary of lists
#------------------------------------------------------

# Runtime:  53.15%
# Memory:   14.51%


class UndergroundSystem:

    def __init__(self):
        # key = id, value = (stationName, time)
        self.travelers = {}
        # key = (startStation, endStation), value = [total_time, trip_count]
        self.travel_data = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.travelers[id]
        time_delta = t - startTime

        key = (startStation, stationName)
        data = self.travel_data[key] if key in self.travel_data else [0, 0]
        
        data[0] += time_delta
        data[1] += 1

        self.travel_data[key] = data


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        total_time, trip_count = self.travel_data[key]
        return total_time / trip_count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)




#------------------------------------------------------
# Solution 2 - dictionary of tuples
#------------------------------------------------------

# Runtime:  73.34%
# Memory:   19.80%


class UndergroundSystem:

    def __init__(self):
        # key = id, value = (stationName, time)
        self.travelers = {}
        # key = (startStation, endStation), value = (total_time, trip_count)
        self.travel_data = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelers[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.travelers[id]
        time_delta = t - startTime

        key = (startStation, stationName)
        data = self.travel_data[key] if key in self.travel_data else (0, 0)
        
        new_data = (data[0] + time_delta, data[1] + 1)
        self.travel_data[key] = new_data


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        total_time, trip_count = self.travel_data[key]
        return total_time / trip_count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)