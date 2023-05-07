#------------------------------------------------------
# Solution 1 - list of courses by len w/ last obstacle
#------------------------------------------------------

# Runtime:   6.60%
# Memory:   19.70%


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []

        # index = len of course, val = last obstacle in the course
        courses_by_length = []

        for obstacle in obstacles:
            if not courses_by_length:
                courses_by_length.append(obstacle)
                result.append(1)
                continue

            insertion_point = len(courses_by_length) - 1
            while courses_by_length[insertion_point] > obstacle and insertion_point >= 0:
                insertion_point -= 1

            insertion_point += 1

            if insertion_point >= len(courses_by_length):
                courses_by_length.append(obstacle)
                result.append(len(courses_by_length))
            else:
                courses_by_length[insertion_point] = obstacle
                result.append(insertion_point + 1)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ modular insertion index
#------------------------------------------------------

# Runtime:   6.60%
# Memory:    9.90%


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        result = []

        # index = len of course, val = last obstacle in the course
        courses_by_length = []


        def findInsertionPoint(obstacle):
            insertion_point = len(courses_by_length) - 1
            while courses_by_length[insertion_point] > obstacle and insertion_point >= 0:
                insertion_point -= 1

            return insertion_point + 1


        for obstacle in obstacles:
            if not courses_by_length:
                courses_by_length.append(obstacle)
                result.append(1)
                continue

            insertion_point = findInsertionPoint(obstacle)

            if insertion_point >= len(courses_by_length):
                courses_by_length.append(obstacle)
                result.append(len(courses_by_length))
            else:
                courses_by_length[insertion_point] = obstacle
                result.append(insertion_point + 1)

        return result