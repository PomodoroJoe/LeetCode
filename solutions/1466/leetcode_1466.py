#------------------------------------------------------
# Solution 1 - variation on depth first search
#------------------------------------------------------

# Runtime:  51.90%
# Memory:   63.24%


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = 0

        roads_to_city = defaultdict(set)    # key = city, value: cities that lead TO this city
        roads_from_city = defaultdict(set)   # key = city, value: cities we can got to FROM this city

        for a, b in connections:
            roads_from_city[a].add(b)
            roads_to_city[b].add(a)

        visited = set()
        queue = [0]

        while queue:
            city = queue.pop()

            if city in visited:
                continue

            visited.add(city)

            for prev_city in roads_to_city[city]:
                if prev_city not in visited:
                    queue.append(prev_city)

            for next_city in roads_from_city[city]:
                if next_city not in visited:
                    result += 1
                    queue.append(next_city)

        return result



#------------------------------------------------------
# Solution 2 - visited array
#------------------------------------------------------

# Runtime:  82.10%
# Memory:   63.14%


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = 0

        roads_to_city = defaultdict(set)    # key = city, value: cities that lead TO this city
        roads_from_city = defaultdict(set)   # key = city, value: cities we can got to FROM this city

        for a, b in connections:
            roads_from_city[a].add(b)
            roads_to_city[b].add(a)

        visited = [False] * n
        queue = [0]

        while queue:
            city = queue.pop()

            if visited[city]:
                continue

            visited[city] = True

            for prev_city in roads_to_city[city]:
                if visited[prev_city] == False:
                    queue.append(prev_city)

            for next_city in roads_from_city[city]:
                if visited[next_city] == False:
                    result += 1
                    queue.append(next_city)

        return result


#------------------------------------------------------
# Solution 3 - single road dictionary
#------------------------------------------------------

# Runtime:  92.29%
# Memory:   79.90%


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = 0
        
        roads = defaultdict(list)   # key = city, value: all roads to/from city

        for road in connections:
            roads[road[0]].append(road)
            roads[road[1]].append(road)

        visited = [False] * n
        queue = [0]

        while queue:
            city = queue.pop()

            if visited[city]:
                continue

            visited[city] = True

            for road in roads[city]:
                if road[1] == city:
                    prev_city = road[0]
                    if visited[prev_city] == False:
                        queue.append(prev_city)
                else:
                    next_city = road[1]
                    if visited[next_city] == False:
                        result += 1
                        queue.append(next_city)

        return result