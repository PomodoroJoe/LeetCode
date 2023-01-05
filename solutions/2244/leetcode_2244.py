#------------------------------------------------------
# Solution 1
#------------------------------------------------------

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        result = 0

        task_mapping = {}
        for task in tasks:
            if task in task_mapping:
                task_mapping[task] += 1
            else:
                task_mapping[task] = 1

        for count in task_mapping.values():
            # count = 3x + 2y (want ot maximize x)
            x = count // 3
            remainder = count % 3

            if remainder == 1 and x > 0:
                x -= 1
                remainder += 3

            if remainder == 1:
                return -1

            y = remainder // 2

            result += (x + y)

        return result


    
#------------------------------------------------------
# Solution 2
#------------------------------------------------------

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        result = 0

        task_mapping = {}
        for task in tasks:
            if task in task_mapping:
                task_mapping[task] += 1
            else:
                task_mapping[task] = 1

        for count in task_mapping.values():

            if count < 2:
                return -1

            # count = 3x + 2y (want ot maximize x)
            x = count // 3
            remainder = count % 3

            if remainder == 0:
                result += x
                continue

            y = 1

            result += (x + y)

        return result
