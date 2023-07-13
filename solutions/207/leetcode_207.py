#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  78.73%
# Memory:   62.20%


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # key = course, value = list of prerequisites
        prereq_map = defaultdict(list)
        for (a, b) in prerequisites:
            prereq_map[a].append(b)

        dp = [None] * numCourses

        def canTakeCourse(course):
            if dp[course] != None:
                return dp[course]

            dp[course] = False

            prereqs = prereq_map[course]
            for prereq in prereqs:
                if not canTakeCourse(prereq):
                    return False

            dp[course] = True
            return True


        for course in range(numCourses):
            visited = set()
            if not canTakeCourse(course):
                return False

        return True




#------------------------------------------------------
# Solution 2 - Solution 1 w/ alternate if block
#------------------------------------------------------

# Runtime:  93.99%
# Memory:   52.20%


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # key = course, value = list of prerequisites
        prereq_map = defaultdict(list)
        for (a, b) in prerequisites:
            prereq_map[a].append(b)

        dp = [None] * numCourses

        def canTakeCourse(course):
            if dp[course] == None:
                dp[course] = False

                for prereq in prereq_map[course]:
                    if not canTakeCourse(prereq):
                        return False

                dp[course] = True
            return dp[course]

        for course in range(numCourses):
            if not canTakeCourse(course):
                return False

        return True