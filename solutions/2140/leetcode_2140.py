#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        max_index = len(questions) - 1

        def mostPointsRecurse(index):
            if index > max_index:
                return 0

            option_1 = mostPointsRecurse(index + 1)

            points, brainpower = questions[index]
            option_2 = points + mostPointsRecurse(index + brainpower + 1)

            return max(option_1, option_2)

        return mostPointsRecurse(0)



#------------------------------------------------------
# Solution 2 - recursive w/ caching
#------------------------------------------------------

# Runtime:   5.76%
# Memory:   16.46%


rom functools import cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        max_index = len(questions) - 1

        @cache
        def mostPointsRecurse(index):
            if index > max_index:
                return 0

            option_1 = mostPointsRecurse(index + 1)

            points, brainpower = questions[index]
            option_2 = points + mostPointsRecurse(index + brainpower + 1)

            return max(option_1, option_2)

        return mostPointsRecurse(0)



#------------------------------------------------------
# Solution 3 - Solution 2 w/ custom max()
#------------------------------------------------------

# Runtime:  12.76%
# Memory:   16.45%


from functools import cache

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        max_index = len(questions) - 1

        @cache
        def mostPointsRecurse(index):
            if index > max_index:
                return 0

            option_1 = mostPointsRecurse(index + 1)

            points, brainpower = questions[index]
            option_2 = points + mostPointsRecurse(index + brainpower + 1)

            return option_1 if option_1 > option_2 else option_2

        return mostPointsRecurse(0)



#------------------------------------------------------
# Solution 4 - Iterative (reverse array)
#------------------------------------------------------

# Runtime:  80.66%
# Memory:   54.73%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]

        for i, q in enumerate(reversed_questions):
            points, brainpower = q

            option_1 = points if not results else results[-1]

            next_question_index = i - brainpower - 1
            option_2 = points + (results[next_question_index] if next_question_index >= 0 else 0)

            results.append(max(option_1, option_2))

        return results[-1]



#------------------------------------------------------
# Solution 5 - Solution 4 w/ custom max()
#------------------------------------------------------

# Runtime:  91.36%
# Memory:   54.73%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]

        for i, q in enumerate(reversed_questions):
            points, brainpower = q

            option_1 = points if not results else results[-1]

            next_question_index = i - brainpower - 1
            option_2 = points + (results[next_question_index] if next_question_index >= 0 else 0)

            results.append(option_1 if option_1 > option_2 else option_2)

        return results[-1]


#------------------------------------------------------
# Solution 6 - Solution 5 w/ short names
#------------------------------------------------------

# Runtime:  95.88%
# Memory:   62.14%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]

        for i, q in enumerate(reversed_questions):
            p, b = q

            option_1 = p if not results else results[-1]

            index = i - b - 1
            option_2 = p + (results[index] if index >= 0 else 0)

            results.append(option_1 if option_1 > option_2 else option_2)

        return results[-1]


#------------------------------------------------------
# Solution 7 - Solution 6 w/ better op_1
#------------------------------------------------------

# Runtime:  90.54%
# Memory:   51.85%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]
        for i, q in enumerate(reversed_questions):
            p, b = q

            op_1 = results[-1] if results else p

            index = i - b - 1
            op_2 = p + (results[index] if index >= 0 else 0)

            results.append(op_1 if op_1 > op_2 else op_2)

        return results[-1]


#------------------------------------------------------
# Solution 8 - Solution 7 w/ fewer empty lines
#------------------------------------------------------

# Runtime:  97.94%
# Memory:   57.20%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]
        for i, q in enumerate(reversed_questions):
            p, b = q
            op_1 = results[-1] if results else p

            index = i - b - 1
            op_2 = p + (results[index] if index >= 0 else 0)
            results.append(op_1 if op_1 > op_2 else op_2)

        return results[-1]


#------------------------------------------------------
# Solution 9 - Solution 8 compact
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   57.20%


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        results = []

        reversed_questions = questions[::-1]
        for i, q in enumerate(reversed_questions):
            p, b = q
            op_1 = results[-1] if results else p

            index = i - b - 1
            op_2 = p + (results[index] if index >= 0 else 0)
            results.append(op_1 if op_1 > op_2 else op_2)

        return results[-1]