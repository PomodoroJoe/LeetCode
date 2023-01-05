#------------------------------------------------------
# Solution 1
#------------------------------------------------------

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        prev_point = sorted_points[0]

        result = len(points)

        for i in range(1, len(points)):
            cur_point = sorted_points[i]

            # overlap?
            if cur_point[0] > prev_point[1] or cur_point[1] < prev_point[0]:
                # no
                prev_point = cur_point
            else:
                result -= 1

                # p1s---------p1e
                #    p2s-----------p2e

                new_start = max(cur_point[0], prev_point[0])
                new_end = min(cur_point[1], prev_point[1])
                prev_point = [new_start, new_end]

        return result



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        cur_end = -inf

        result = 0
       
        for point in points:
            if point[0] > cur_end:
                result += 1
                cur_end = point[1]

        return result
