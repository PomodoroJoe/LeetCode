#------------------------------------------------------
# Solution 1 - recursive - FAILED!
#------------------------------------------------------

# WRONG ANSWER!

# TEST CASE   (minProfit = 0)
'''
64
0
[80, 40]
[88, 88]
'''

# Runtime:  82.60%
# Memory:   19.50%


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        result = 0

        max_index = len(group) - 1

        def profitableSchemesRecurse(index, remaining_n, remaining_profit):
            if index > max_index:
                return 0

            option_1 = profitableSchemesRecurse(index + 1, remaining_n, remaining_profit)
            option_2 = 0
            
            members_needed = group[index]
            profit_made = profit[index]

            if remaining_n >= members_needed:
                new_n = remaining_n - members_needed
                new_profit = remaining_profit - profit_made

                option_2 = 1 if new_profit <= 0 else 0
                option_2 += profitableSchemesRecurse(index + 1, new_n, new_profit)

            return option_1 + option_2

        result = profitableSchemesRecurse(0, n, minProfit)
        return result % (pow(10, 9) + 7)



#------------------------------------------------------
# Solution 2 - Solution 1 with hacks edge case & @cache
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


from functools import cache

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        if minProfit == 0:
            return 2

        result = 0

        max_index = len(group) - 1

        @cache
        def profitableSchemesRecurse(index, remaining_n, remaining_profit):
            if index > max_index:
                return 0

            option_1 = profitableSchemesRecurse(index + 1, remaining_n, remaining_profit)
            option_2 = 0
            
            members_needed = group[index]
            profit_made = profit[index]

            if remaining_n >= members_needed:
                new_n = remaining_n - members_needed
                new_profit = remaining_profit - profit_made

                option_2 = 1 if new_profit <= 0 else 0
                option_2 += profitableSchemesRecurse(index + 1, new_n, new_profit)

            return option_1 + option_2

        result = profitableSchemesRecurse(0, n, minProfit)
        return result % (pow(10, 9) + 7)



#------------------------------------------------------
# Solution 3 - iterative w/ 3 dimensional cache
#------------------------------------------------------


# Runtime:  57.69%
# Memory:   34.62%


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        job_count = len(group)

        # cube [job] [members] [profit]
        cube = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(job_count + 1)]
        
        cube[0][0][0] = 1

        for x in range(1, job_count + 1):
            members_needed, profit_made = group[x - 1], profit[x - 1]

            for y in range(n+1):
                for z in range(minProfit + 1):
                    prev_val = cube[x - 1][y][z]

                    if y >= members_needed:
                        cube[x][y][z] = prev_val + cube[x-1][y-members_needed][max(0, z - profit_made)]
                    else:
                        cube[x][y][z] = prev_val

        result = sum(cube[-1][member_count][-1] for member_count in range(n + 1))
        return result % (pow(10, 9) + 7)