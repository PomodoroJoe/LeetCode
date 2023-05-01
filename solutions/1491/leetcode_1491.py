#------------------------------------------------------
# Solution 1 - one line
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21%


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)



#------------------------------------------------------
# Solution 2
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21%


class Solution:
    def average(self, salary: List[int]) -> float:
        
        total = 0
        min_value = 1000001
        max_value = 0

        index = 0
        max_index = len(salary) - 1

        while index <= max_index:
            val = salary[index]

            total = total + val

            if val < min_value:
                min_value = val

            if val > max_value:
                max_value = val

            index = index + 1

        total = total - (min_value + max_value)

        number_of_values = len(salary) - 2

        return total / number_of_values



#------------------------------------------------------
# Solution 3
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21%


class Solution:
    def average(self, salary: List[int]) -> float:
        
        total = 0
        min_value = 1000001
        max_value = 0

        index = 0
        max_index = len(salary) - 1

        while index <= max_index:
            val = salary[index]
            total += val

            if val < min_value:
                min_value = val
            if val > max_value:
                max_value = val
            index += 1



#------------------------------------------------------
# Solution 4
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21%


class Solution:
    def average(self, salary: List[int]) -> float:
        sorted_salary = sorted(salary)

        sorted_salary.pop(0)
        sorted_salary.pop(-1)

        return sum(sorted_salary) / len(sorted_salary)


#------------------------------------------------------
# Solution 5
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21


class Solution:
    def average(self, salary: List[int]) -> float:
        
        salary_copy = salary.copy()

        min_value = min(salary)
        max_value = max(salary)

        salary_copy.remove(min_value)
        salary_copy.remove(max_value)

        return sum(salary_copy) / len(salary_copy)



#------------------------------------------------------
# Solution 6
#------------------------------------------------------

# Runtime:   5.49%
# Memory:    8.21


class Solution:
    def average(self, salary: List[int]) -> float:
        min_value = min(salary)
        max_value = max(salary)

        salary.remove(min_value)
        salary.remove(max_value)

        return sum(salary) / len(salary)
