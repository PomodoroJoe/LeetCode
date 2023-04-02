#------------------------------------------------------
# Solution 1 - simple thing first
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []

        for spell in spells:
            count = 0
            for potion in potions:
                if spell * potion >= success:
                    count +=1

            result.append(count)

        return result



#------------------------------------------------------
# Solution 2 - potions delta (total - unsuccessful)
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []

        sorted_potions = sorted(potions)
        potions_count = len(potions)

        for spell in spells:
            count = 0
            for potion in sorted_potions:
                if spell * potion < success:
                    count +=1
                    continue
                break

            result.append(potions_count - count)

        return result


#------------------------------------------------------
# Solution 3 - potions delta w/ binary search
#------------------------------------------------------

# Runtime:  35.12%
# Memory:   50.42%


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []

        sorted_potions = sorted(potions)
        total_potions = len(potions)

        def binarySearch(spell):
            low = 0
            high = total_potions

            while low < high:
                mid = low + (high - low) // 2

                if sorted_potions[mid] * spell < success:
                    low = mid + 1
                else:
                    high = mid

            return low


        for spell in spells:
            count = binarySearch(spell)
            result.append(total_potions - count)

        return result



#------------------------------------------------------
# Solution 4 - potions delta w/ binary search (no count)
#------------------------------------------------------

# Runtime:  43.34%
# Memory:   50.42%


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []

        sorted_potions = sorted(potions)
        total_potions = len(potions)

        def binarySearch(spell):
            low = 0
            high = total_potions

            while low < high:
                mid = low + (high - low) // 2

                if sorted_potions[mid] * spell < success:
                    low = mid + 1
                else:
                    high = mid

            return low


        for spell in spells:
            result.append(total_potions - binarySearch(spell))

        return result



#------------------------------------------------------
# Solution 5 - Solution 4 w/ preallocated result
#------------------------------------------------------

# Runtime:  35.97%
# Memory:   50.42%


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = [0] * len(spells)

        sorted_potions = sorted(potions)
        total_potions = len(potions)

        def binarySearch(spell):
            low = 0
            high = total_potions

            while low < high:
                mid = low + (high - low) // 2

                if sorted_potions[mid] * spell < success:
                    low = mid + 1
                else:
                    high = mid

            return low


        for i, spell in enumerate(spells):
            result[i] = (total_potions - binarySearch(spell))

        return result