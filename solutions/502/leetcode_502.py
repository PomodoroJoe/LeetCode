#------------------------------------------------------
# Solution 1 - first attempt
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        result = w

        # find projects we can do - capital[i] <= result
        # sort by profit - select project with greatest profit
        # continue until we have k projects or no projects we can do

        projects = []

        for i in range(len(capital)):
            c = capital[i]
            p = profits[i]

            projects.append((c, p))

        # sort by capital requirements
        projects.sort()

        project_options = []
        project_index = 0
        project_count = 0

        # continue until we have k projects or no projects we can do
        while project_count < k:

            # find projects we can do - capital[i] <= result
            while project_index < len(projects) and projects[project_index][0] <= result:
                project_options.append(projects[project_index][1])
                project_index += 1

            if not project_options:
                break

            # sort by profit
            project_options.sort()

            result += project_options.pop(-1)
            project_count += 1

        return result



#------------------------------------------------------
# Solution 2 - max heap
#------------------------------------------------------

# Runtime:  45.60%
# Memory:   19.41%



from heapq import heappush, heappop, heapify

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        result = w

        # find projects we can do - capital[i] <= result
        # sort by profit - select project with greatest profit
        # continue until we have k projects or no projects we can do

        projects = []

        for i in range(len(capital)):
            c = capital[i]
            p = profits[i]

            projects.append((c, p))

        # sort by capital requirements
        projects.sort()

        project_options = []    # heap
        project_index = 0
        project_count = 0

        # continue until we have k projects or no projects we can do
        while project_count < k:

            # find projects we can do - capital[i] <= result
            while project_index < len(projects) and projects[project_index][0] <= result:
                #project_options.append(projects[project_index][1])
                heappush(project_options, -projects[project_index][1])
                project_index += 1

            if not project_options:
                break

            # sort by profit
            #project_options.sort()

            #result += project_options.pop(-1)
            result += -heappop(project_options)
            project_count += 1

        return result



#------------------------------------------------------
# Solution 3 - max heap w/ early return
#------------------------------------------------------


# Runtime:  98.44%
# Memory:   86.83%


from heapq import heappush, heappop, heapify, nlargest

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        if w >= max(capital):
            return sum(nlargest(k, profits)) + w

        result = w

        # find projects we can do - capital[i] <= result
        # sort by profit - select project with greatest profit
        # continue until we have k projects or no projects we can do

        projects = []

        for i in range(len(capital)):
            c = capital[i]
            p = profits[i]

            projects.append((c, p))

        # sort by capital requirements
        projects.sort()

        project_options = []    # heap
        project_index = 0
        project_count = 0

        # continue until we have k projects or no projects we can do
        while project_count < k:

            # find projects we can do - capital[i] <= result
            while project_index < len(projects) and projects[project_index][0] <= result:
                #project_options.append(projects[project_index][1])
                heappush(project_options, -projects[project_index][1])
                project_index += 1

            if not project_options:
                break

            # sort by profit
            #project_options.sort()

            #result += project_options.pop(-1)
            result += -heappop(project_options)
            project_count += 1

        return result