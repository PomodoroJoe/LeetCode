#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime: 60.79%
# Memory:  10.40%

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        '''
        (y1 - y2) / [x1 - x2] = [y - y1] / [x - x1] --> 

        [y - y1] = ([y1 - y2] / [x1 - x2] ) [x - x1]

        y = ([y1 - y2] / [x1 - x2]) [x - x1] + y1
        '''

        result = 1
        lines = {}  # equation : set of points

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]

                slope = None

                # vertical
                if p1[0] == p2[0]:
                    slope = inf
                    c = p1[0]

                # horizontal
                if p1[1] == p2[1]:
                    slope = 0
                    c = p1[1]

                if slope == None:
                    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
                    c = (slope * -p1[0]) + p1[1]

                key = (slope, c)
                if key in lines:
                    lines[key].add(tuple(p1))
                    lines[key].add(tuple(p2))
                else:
                    lines[key] = set()
                    lines[key].add(tuple(p1))
                    lines[key].add(tuple(p2))

        for key in lines:
            result = max(result, len(lines[key]))

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime: 67.18%
# Memory:   8.91%

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        result = 1
        lines = {}  # equation : set of points

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = tuple(points[i])
                p2 = tuple(points[j])

                slope = None

                # vertical
                if p1[0] == p2[0]:
                    slope = inf
                    c = p1[0]

                    key = (slope, c)
                    if key not in lines:
                        lines[key] = set()

                    lines[key].add(p1)
                    lines[key].add(p2)
                    continue

                # horizontal
                if p1[1] == p2[1]:
                    slope = 0
                    c = p1[1]

                    key = (slope, c)
                    if key not in lines:
                        lines[key] = set()

                    lines[key].add(p1)
                    lines[key].add(p2)
                    continue

                if slope == None:
                    slope = (p1[1] - p2[1]) / (p1[0] - p2[0])
                    c = (slope * -p1[0]) + p1[1]

                key = (slope, c)
                if key not in lines:
                    lines[key] = set()

                lines[key].add(p1)
                lines[key].add(p2)

        for key in lines:
            result = max(result, len(lines[key]))

        return result
