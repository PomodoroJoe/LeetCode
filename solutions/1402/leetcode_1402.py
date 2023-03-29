#------------------------------------------------------
# Solution 1 - sort dishes and update list
#------------------------------------------------------

# Runtime:  41.46%
# Memory:   46.84%


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0

        sorted_dishes = sorted(satisfaction)
        max_index = len(sorted_dishes) - 1

        index = 0
        while index < max_index and sorted_dishes[index] < 0:
            index += 1

        current = sorted_dishes[index:]

        def score_dishes(dishes):
            time = 1
            score = 0
            for dish in dishes:
                score += time * dish
                time += 1
            return score

        result = max(result, score_dishes(current))

        while index > 0:
            index -= 1
            current = [sorted_dishes[index]] + current
            result = max(result, score_dishes(current))

        return result




#------------------------------------------------------
# Solution 2 - sort dishes & update list in single loop
#------------------------------------------------------

# Runtime:  37.97%
# Memory:   77.85%


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0

        sorted_dishes = sorted(satisfaction)
        max_index = len(sorted_dishes) - 1

        def score_dishes(dishes):
            time = 1
            score = 0
            for dish in dishes:
                score += time * dish
                time += 1
            return score

        index = max_index
        current = []

        while index >= 0:
            current = [sorted_dishes[index]] + current
            result = max(result, score_dishes(current))
            index -= 1

        return result




#------------------------------------------------------
# Solution 3 - sort dishes and update score with math
#------------------------------------------------------

# Runtime:  61.39%
# Memory:   98.73%


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0

        sorted_dishes = sorted(satisfaction)
        max_index = len(sorted_dishes) - 1

        index = max_index

        current_sum = 0
        prev_score = 0

        while index >= 0:
            current_sum += sorted_dishes[index]
            current_score = current_sum + prev_score
            prev_score = current_score

            result = max(result, current_score)

            # [A]           A                   A                           A
            # [B, A]        B + 2A              B + A + A                   (B + A) + A
            # [C, B, A]     C + 2B + 3A         C + B + B + A + A + A       (C + B + A) + ((B + A) + A)

            index -= 1

        return result



#------------------------------------------------------
# Solution 4 - sort dishes, use math, early return
#------------------------------------------------------

# Runtime:  95.57%
# Memory:   46.84%


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0

        sorted_dishes = sorted(satisfaction)
        index = len(sorted_dishes) - 1

        current_sum = 0
        prev_score = 0

        while index >= 0:
            current_sum += sorted_dishes[index]
            current_score = current_sum + prev_score
            prev_score = current_score

            if result < current_score:
                result = current_score
            else:
                break

            index -= 1

        return result
