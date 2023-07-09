#------------------------------------------------------
# Solution 1 - Kadane's Algorithm Variation
#------------------------------------------------------

# Runtime:  69.23%
# Memory:   25.64%


class Solution:
    def largestVariance(self, s: str) -> int:
        result = 0

        letters = "abcdefghijklmnopqrstuvwxyz"
        
        for max_letter_index in range(len(letters)):
            for min_letter_index in range(len(letters)):

                if min_letter_index == max_letter_index:
                    continue
                
                max_letter = letters[max_letter_index]
                min_letter = letters[min_letter_index]

                max_count = 0
                min_count = 0
                min_letter_found = False

                for letter in s:
                    if letter == max_letter:
                        max_count += 1
                    elif letter == min_letter:
                        min_count += 1
                        min_letter_found = True
                    else:
                        continue

                    if min_count == 0:
                        continue

                    if max_count - min_count < 0:
                        max_count = 0
                        min_count = 0
                    else:
                        result = max(result, max_count - min_count)

                if min_letter_found and max_count > 1 and min_count == 0:
                    result = max(result, max_count - 1)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ reduced character list
#------------------------------------------------------

# Runtime:  92.31%
# Memory:   25.64%


class Solution:
    def largestVariance(self, s: str) -> int:
        result = 0

        letters = list(set(s))
        
        for max_letter_index in range(len(letters)):
            for min_letter_index in range(len(letters)):

                if min_letter_index == max_letter_index:
                    continue
                
                max_letter = letters[max_letter_index]
                min_letter = letters[min_letter_index]

                max_count = 0
                min_count = 0
                min_letter_found = False

                for letter in s:
                    if letter == max_letter:
                        max_count += 1
                    elif letter == min_letter:
                        min_count += 1
                        min_letter_found = True
                    else:
                        continue

                    if min_count == 0:
                        continue

                    if max_count - min_count < 0:
                        max_count = 0
                        min_count = 0
                    else:
                        result = max(result, max_count - min_count)

                if min_letter_found and max_count > 1 and min_count == 0:
                    result = max(result, max_count - 1)

        return result