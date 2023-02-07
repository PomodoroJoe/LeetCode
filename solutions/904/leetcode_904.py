#------------------------------------------------------
# Solution 1 - naive
#------------------------------------------------------

# TIME LIMIE EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0

        for start_tree in range(len(fruits)):
            
            count = 0
            baskets = set()

            for tree in range(start_tree, len(fruits)):
                fruit = fruits[tree]

                baskets.add(fruit)
                if len(baskets) > 2:
                    break

                count += 1
            result = max(result, count)

        return result




#------------------------------------------------------
# Solution 2 - naive w/ reduced starting tree range
#------------------------------------------------------

# Runtime:  24.75%
# Memory:   13.34%


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        result = 0

        start_tree = 0
        while start_tree < len(fruits) - result:
            
            count = 0
            baskets = set()

            for tree in range(start_tree, len(fruits)):
                fruit = fruits[tree]

                baskets.add(fruit)
                if len(baskets) > 2:
                    break

                count += 1
                
            result = max(result, count)
            start_tree += 1

        return result