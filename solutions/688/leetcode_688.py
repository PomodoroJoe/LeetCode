#------------------------------------------------------
# Solution 1 - dynamic programming
#------------------------------------------------------

# Runtime:  19.37%
# Memory:   55.21%


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # [Move][Row][Column]
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]

        dp[0][row][column] = 1.0

        move_deltas = [
            ( 2, -1), ( 2,  1),
            (-2, -1), (-2,  1),
            ( 1, -2), ( 1,  2),
            (-1, -2), (-1,  2)
        ]

        for move in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for delta in move_deltas:
                        prev_r = r - delta[0]
                        prev_c = c - delta[1]

                        if prev_r < 0 or prev_r >= n or prev_c < 0 or prev_c >= n:
                            continue

                        dp[move][r][c] += dp[move - 1][prev_r][prev_c]

                    dp[move][r][c] = dp[move][r][c] / 8


        result = 0

        for row in dp[k]:
            result += sum(row)

        return result


#------------------------------------------------------
# Solution 2 - Solution 1 w/o continue
#------------------------------------------------------

# Runtime:  27.12%
# Memory:   62.23%


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # [Move][Row][Column]
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]

        dp[0][row][column] = 1.0

        move_deltas = [
            ( 2, -1), ( 2,  1),
            (-2, -1), (-2,  1),
            ( 1, -2), ( 1,  2),
            (-1, -2), (-1,  2)
        ]

        for move in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for delta in move_deltas:
                        prev_r = r - delta[0]
                        prev_c = c - delta[1]

                        if prev_r >= 0 and prev_r < n and prev_c >= 0 and prev_c < n:
                            dp[move][r][c] += dp[move - 1][prev_r][prev_c]

                    dp[move][r][c] = dp[move][r][c] / 8


        result = 0

        for row in dp[k]:
            result += sum(row)

        return result