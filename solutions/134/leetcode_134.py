#------------------------------------------------------
# Solution 1
#------------------------------------------------------

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station_count = len(gas)
        
        for start_station in range(station_count):
            station = start_station
            tank = 0

            while True:
                tank += gas[station]
                tank -= cost[station]

                station = (station + 1) % station_count

                if tank < 0:
                    break

                if station == start_station:
                    return start_station

        return -1



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        station_count = len(gas)
        
        start_station = 0
        while start_station < station_count:
            station = start_station
            tank = 0

            while True:
                tank += gas[station]
                tank -= cost[station]

                station = (station + 1) % station_count

                if tank < 0:
                    start_station = station if station > start_station else station_count
                    break

                if station == start_station:
                    return start_station

        return -1
