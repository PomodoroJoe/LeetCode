#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  73.51%
# Memory:   72.92%


class Solution:
    def bestClosingTime(self, customers: str) -> int:

        # penalty for staying open all hours
        base_penalty = 0
        for c in customers:
            if c == 'N':
                base_penalty += 1

        hours = len(customers)

        result = hours
        best_penalty = base_penalty
        current_penalty = base_penalty

        # try closing the store 1 hour earlier (each time through the loop)
        for h in range(hours - 1, -1, -1):
            if customers[h] == 'Y':
                current_penalty += 1
            else:
                current_penalty -= 1

            if current_penalty <= best_penalty:
                result = h
                best_penalty = current_penalty

        return result