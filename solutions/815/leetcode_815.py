#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  50.80%
# Memory:   12.30%


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        start_buses = set()
        connected_buses = [set() for _ in routes]
        bus_stops = [None for _ in routes]

        for bus, stops in enumerate(routes):
            bus_stops[bus] = set(stops)

            if source in bus_stops[bus]:
                start_buses.add(bus)

        bus_count = len(routes)

        for bus in range(bus_count):
            for next_bus in range(bus + 1, bus_count):
                if bus_stops[bus].intersection(bus_stops[next_bus]):
                        connected_buses[bus].add(next_bus)
                        connected_buses[next_bus].add(bus)

        cache = {}

        def numBusesToDestinationRecurse(bus, used_buses = set()):
            if target in routes[bus]:
                return 1

            if bus in cache:
                return cache[bus]

            new_used_buses = used_buses.copy()
            new_used_buses.add(bus)

            result = inf

            for next_bus in connected_buses[bus]:
                if next_bus in new_used_buses:
                    continue

                option = numBusesToDestinationRecurse(next_bus, new_used_buses)
                if option == inf:
                    continue

                option += 1
                result = min(result, option)

            cache[bus] = result
            return result


        result = inf

        for bus in start_buses:
            option = numBusesToDestinationRecurse(bus)
            result = min(result, option)

        return result if result != inf else -1