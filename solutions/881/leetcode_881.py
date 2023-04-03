#------------------------------------------------------
# Solution 1 - sorted weights with two pointers
#------------------------------------------------------

# Runtime:  86.50%
# Memory:   18.19%


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        sorted_people = sorted(people)

        low = 0
        high = len(people) - 1

        result = 0

        while low <= high:
            if sorted_people[low] + sorted_people[high] <= limit:
                low += 1
                
            high -= 1
            result += 1

        return result



#------------------------------------------------------
# Solution 2 - sort weights in-place with two pointers
#------------------------------------------------------

# Runtime:  73.60%
# Memory:   96.73%


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        low = 0
        high = len(people) - 1

        result = 0

        while low <= high:
            if people[low] + people[high] <= limit:
                low += 1
                
            high -= 1
            result += 1

        return result



#------------------------------------------------------
# Solution 3 - same as 1 w/o extra whitespace
#------------------------------------------------------

# Runtime:  95.10%
# Memory:   60.46%


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        sorted_people = sorted(people)

        low = 0
        high = len(people) - 1

        result = 0

        while low <= high:
            if sorted_people[low] + sorted_people[high] <= limit:
                low += 1
            high -= 1
            result += 1

        return result