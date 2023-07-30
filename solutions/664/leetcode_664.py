#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  85.24%
# Memory:   46.31%


class Solution:
    def strangePrinter(self, s: str) -> int:

        @cache
        def strangePrinterRecurse(left_index, right_index):
            if left_index > right_index:
                return 0

            result = 1 + strangePrinterRecurse(left_index, right_index - 1)

            for split in range(left_index, right_index):
                if s[split] == s[right_index]:
                    option = strangePrinterRecurse(left_index, split)
                    option += strangePrinterRecurse(split + 1, right_index - 1)
                    result = min(result, option)

            return result


        return strangePrinterRecurse(0, len(s) - 1)