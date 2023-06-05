#------------------------------------------------------
# Solution 1 - union find
#------------------------------------------------------

# Runtime:  88.57%
# Memory:   71.99%


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = [x for x in range(n + 1)]

        def find(city):
            province = provinces[city]
            if city == province:
                return province
            return find(province)

        def union(city1, city2):
            province = find(city1)
            next_city = provinces[city2]

            provinces[city2] = province
            if next_city != province:
                union(province, next_city)


        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)

        province_count = 0

        for i in range(n):
            if i == provinces[i]:
                province_count += 1

        return province_count