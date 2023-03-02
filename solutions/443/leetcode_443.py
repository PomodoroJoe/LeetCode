#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  99.30%
# Memory:   65.10%


class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0

        char = chars[0]
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == char:
                count += 1
            else:
                chars[pos] = char
                pos += 1

                if count > 1:
                    count_string = str(count)
                    for c in count_string:
                        chars[pos] = c
                        pos += 1

                char = chars[i]
                count = 1

        chars[pos] = char
        pos += 1

        if count > 1:
            count_string = str(count)
            for c in count_string:
                chars[pos] = c
                pos += 1

        return pos