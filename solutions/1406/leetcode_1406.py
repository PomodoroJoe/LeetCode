#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        max_index = len(stoneValue) - 1

        def stoneGameRecurse(index, remaining_points):
            result = -inf

            if index > max_index:
                return 0

            points = 0

            for i in range(3):
                current_index = index + i
                if current_index > max_index:
                    continue

                points += stoneValue[current_index]

                op = stoneGameRecurse(current_index + 1, remaining_points - points)
                result = max(result, remaining_points - op)

            return result


        total_points = sum(stoneValue)

        alice_points = stoneGameRecurse(0, total_points)
        bob_points = total_points - alice_points

        if alice_points > bob_points: return "Alice"
        if bob_points > alice_points: return "Bob"
        return "Tie"



#------------------------------------------------------
# Solution 2 - Solution 1 w/ cache
#------------------------------------------------------

# Runtime:  33.19%
# Memory:    7.63%


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        max_index = len(stoneValue) - 1

        @cache
        def stoneGameRecurse(index, remaining_points):
            result = -inf

            if index > max_index:
                return 0

            points = 0

            for i in range(3):
                current_index = index + i
                if current_index > max_index:
                    continue

                points += stoneValue[current_index]

                op = stoneGameRecurse(current_index + 1, remaining_points - points)
                result = max(result, remaining_points - op)

            return result


        total_points = sum(stoneValue)

        alice_points = stoneGameRecurse(0, total_points)
        bob_points = total_points - alice_points

        if alice_points > bob_points: return "Alice"
        if bob_points > alice_points: return "Bob"
        return "Tie"



#------------------------------------------------------
# Solution 3 - iterative w/ dp
#------------------------------------------------------

# Runtime:  93.72%
# Memory:   57.85%


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        stone_count = len(stoneValue)

        dp = [0] * (stone_count + 1)

        # dp[i] = best[ stoneValue[i] - dp[i + 1]]...]
        # + ALICE, - BOB, 0 = Tie

        for i in range(stone_count - 1, -1, -1):
            op1 = stoneValue[i] - dp[i + 1]
            dp[i] = op1

            if (i + 1) < stone_count:
                op2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                dp[i] = max(dp[i], op2)

            if (i + 2) < stone_count:
                op3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                dp[i] = max(dp[i], op3)

        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"


#------------------------------------------------------
# Solution 4 - Solution 3 w/ custom max
#------------------------------------------------------

# Runtime:  97.31%
# Memory:   53.81%


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        stone_count = len(stoneValue)

        dp = [0] * (stone_count + 1)

        # dp[i] = best[ stoneValue[i] - dp[i + 1]]...]
        # + ALICE, - BOB, 0 = Tie

        for i in range(stone_count - 1, -1, -1):
            op1 = stoneValue[i] - dp[i + 1]
            best_score = op1

            if (i + 1) < stone_count:
                op2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                best_score = best_score if best_score > op2 else op2

            if (i + 2) < stone_count:
                op3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                best_score = best_score if best_score > op3 else op3

            dp[i] = best_score

        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"