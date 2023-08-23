#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  25.35%
# Memory:   99.70%


class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""

        # key = letter, value = count
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        def getNextLetter(prev_letter):
            letter = None
            current_count = 0

            for c in counts:
                if c == prev_letter:
                    continue

                if counts[c] > current_count:
                    letter = c
                    current_count = counts[c]

            counts[letter] -= 1
            return letter


        while len(result) < len(s):
            prev_letter = result[-1] if result else None

            next_letter = getNextLetter(prev_letter)

            if not next_letter:
                return ""

            result = result + next_letter

        return result



#------------------------------------------------------
# Solution 3
#------------------------------------------------------

# Runtime:  33.47%
# Memory:   46.15%


class Solution:
    def reorganizeString(self, s: str) -> str:
        result = ""
        counts = defaultdict(int)

        for c in s:
            counts[c] += 1

        counts[None] = 0

        def getNextLetter(prev_letter):
            letter = None
            for c in counts:
                if c == prev_letter:
                    continue
                if counts[c] > counts[letter]:
                    letter = c
            counts[letter] -= 1
            return letter


        while len(result) < len(s):
            prev_letter = result[-1] if result else None
            next_letter = getNextLetter(prev_letter)
            if not next_letter:
                return ""
            result = result + next_letter

        return result