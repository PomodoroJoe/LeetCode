#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  60.46%
# Memory:   31.27%


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time_to_reach_city = []
        
        for i in range(len(dist)):
            t = dist[i] / speed[i]
            time_to_reach_city.append(t)

        time_to_reach_city.sort()

        monster = 0

        while monster < len(time_to_reach_city) and monster < time_to_reach_city[monster]:
            monster += 1

        return monster



#------------------------------------------------------
# Solution 2 - Solution 1 w/ len
#------------------------------------------------------

# Runtime:  81.14%
# Memory:   10.85%


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        n = len(speed)
        time_to_reach_city = []
        
        for i in range(n):
            t = dist[i] / speed[i]
            time_to_reach_city.append(t)

        time_to_reach_city.sort()

        monster = 0

        while monster < n and monster < time_to_reach_city[monster]:
            monster += 1

        return monster