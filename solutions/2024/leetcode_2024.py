#------------------------------------------------------
# Solution 1 - sliding window
#------------------------------------------------------

# Runtime:  80.72%
# Memory:   55.12%


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0

        T_count = 0
        F_count = 0

        start = 0
        end = 0

        for end in range(len(answerKey)):
            answer = answerKey[end]
            if answer == 'T':
                T_count += 1
            else:
                F_count += 1

            min_count = min(T_count, F_count)

            if min_count <= k:
                result = max(result, (end - start) + 1)
                continue

            while min_count > k:
                answer = answerKey[start]
                if answer == 'T':
                    T_count -= 1
                else:
                    F_count -= 1

                start += 1
                min_count = min(T_count, F_count)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ custom min/max
#------------------------------------------------------

# Runtime:  95.78%
# Memory:   55.12%


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0

        T_count = 0
        F_count = 0

        start = 0
        end = 0

        for end in range(len(answerKey)):
            answer = answerKey[end]
            if answer == 'T':
                T_count += 1
            else:
                F_count += 1

            min_count = T_count if T_count < F_count else F_count

            if min_count <= k:
                option = (end - start) + 1
                result = option if option > result else result
                continue

            while min_count > k:
                answer = answerKey[start]
                if answer == 'T':
                    T_count -= 1
                else:
                    F_count -= 1

                start += 1
                min_count = T_count if T_count < F_count else F_count

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 w/ counts dictionary
#------------------------------------------------------

# Runtime:  87.65%
# Memory:   55.12%


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        result = 0

        T_count = 0
        F_count = 0

        start = 0
        counts = {'T': 0, 'F': 0}

        for end in range(len(answerKey)):
            key = answerKey[end]
            counts[key] += 1

            min_count = counts['T'] if counts['T'] < counts['F'] else counts['F']

            if min_count <= k:
                option = (end - start) + 1
                result = option if option > result else result
                continue

            while min_count > k:
                key = answerKey[start]
                counts[key] -= 1

                start += 1
                min_count = counts['T'] if counts['T'] < counts['F'] else counts['F']

        return result