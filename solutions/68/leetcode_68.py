#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  87.98%
# Memory:   93.67%


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        last_index = len(words) - 1

        word_length = []
        for word in words:
            word_length.append(len(word))


        def getEndIndexForLine(start_index):
            end_index = start_index
            char_count = 0

            while char_count < maxWidth and end_index <= last_index:
                char_count += word_length[end_index] + 1
                end_index += 1

            end_index -= 1
            char_count -= 1

            if char_count > maxWidth:
                end_index -= 1

            return end_index


        def getLine(start_index, end_index):
            line = ""

            word_count = (end_index - start_index) + 1
            char_count = sum(word_length[start_index:end_index + 1])

            spaces_count = maxWidth - char_count
            gap_count = word_count - 1

            spaces_per_gap = spaces_count // gap_count if gap_count else 0
            extra_spaces = spaces_count - (spaces_per_gap * gap_count)

            if end_index == last_index:
                spaces_per_gap = 1
                extra_spaces = 0

            for word in words[start_index:end_index]:
                line += word
                line += (" " * spaces_per_gap)

                if extra_spaces > 0:
                    line += " "
                    extra_spaces -= 1

            line += words[end_index]

            if len(line) < maxWidth:
                line += " " * (maxWidth - len(line))

            return line


        start_index = 0
        end_index = 0

        while end_index <= last_index:
            end_index = getEndIndexForLine(start_index)
            line = getLine(start_index, end_index)
            result.append(line)

            start_index = end_index + 1
            end_index = start_index

        return result