#------------------------------------------------------
# Solution 1 - recursive w/ cache
#------------------------------------------------------

# Runtime:  90.11%
# Memory:    5.70%


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        result = 0

        @cache
        def timeToInform(id):
            manager_id = manager[id]

            if manager_id == -1:
                return 0

            return informTime[manager_id] + timeToInform(manager_id)


        for id in range(n):
            time = timeToInform(id)
            result = time if time > result else result

        return result



#------------------------------------------------------
# Solution 2 - recursive w/ dp memoization
#------------------------------------------------------

# Runtime:  88.90%
# Memory:    5.70%


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        result = 0

        dp = defaultdict(int)

        def timeToInform(id):
            if id in dp:
                return dp[id]

            manager_id = manager[id]

            if manager_id == -1:
                dp[id] = 0
                return 0

            dp[id] = informTime[manager_id] + timeToInform(manager_id)
            return dp[id]


        for id in range(n):
            time = timeToInform(id)
            result = time if time > result else result

        return result