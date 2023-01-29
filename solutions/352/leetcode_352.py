
#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:   5.19%
# Memory:   76.30%


class SummaryRanges:

    def __init__(self):
        self.stream = [0] * 10001
        

    def addNum(self, value: int) -> None:
        self.stream[value] = 1
        

    def getIntervals(self) -> List[List[int]]:
        result = []
        current_interval = None

        for index, value in enumerate(self.stream):
            if value == 0:
                if current_interval:
                    result.append(current_interval)
                    current_interval = None
                continue

            if not current_interval:
                current_interval = [index, index]
            else:
                current_interval[1] = index

        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()




#------------------------------------------------------
# Solution 2 - w/ cache
#------------------------------------------------------

# Runtime:  14.61%
# Memory:   43.83%


class SummaryRanges:

    def __init__(self):
        self.stream = [0] * 10001
        self.result_cache = None
        

    def addNum(self, value: int) -> None:
        if self.stream[value] == 1:
            return

        self.stream[value] = 1
        self.result_cache = None
        

    def getIntervals(self) -> List[List[int]]:
        if self.result_cache != None:
            return self.result_cache

        result = []
        current_interval = None

        for index, value in enumerate(self.stream):
            if value == 0:
                if current_interval:
                    result.append(current_interval)
                    current_interval = None
                continue

            if not current_interval:
                current_interval = [index, index]
            else:
                current_interval[1] = index

        self.result_cache = result
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()




#------------------------------------------------------
# Solution 3 w/ cache & interval mapping
#------------------------------------------------------

# Runtime:  99.35%
# Memory:   43.83%


class SummaryRanges:

    def __init__(self):
        self.stream = [0] * 10001
        self.result_cache = None

        self.start_to_end_mapping = {}
        self.end_to_start_mapping = {}
        

    def addNum(self, value: int) -> None:
        if self.stream[value] == 1:
            return

        self.stream[value] = 1
        self.result_cache = None

        lower = value - 1
        upper = value + 1

        has_lower = self.stream[lower] if value > 0 else 0
        has_upper = self.stream[upper] if value < 10000 else 0

        if not has_lower and not has_upper:
            self.start_to_end_mapping[value] = value
            self.end_to_start_mapping[value] = value
            return

        if has_lower and has_upper:
            lower_start = self.end_to_start_mapping[lower]
            lower_end = lower

            upper_start = upper
            upper_end = self.start_to_end_mapping[upper]

            new_start = lower_start
            new_end = upper_end

            del self.start_to_end_mapping[upper]
            del self.end_to_start_mapping[lower]

            self.start_to_end_mapping[new_start] = new_end
            self.end_to_start_mapping[new_end] = new_start

            return

        if has_lower:
            lower_start = self.end_to_start_mapping[lower]
            new_end = value

            del self.end_to_start_mapping[lower]

            self.start_to_end_mapping[lower_start] = new_end
            self.end_to_start_mapping[new_end] = lower_start

        if has_upper:
            new_start = value
            upper_end = self.start_to_end_mapping[upper]

            del self.start_to_end_mapping[upper]

            self.start_to_end_mapping[new_start] = upper_end
            self.end_to_start_mapping[upper_end] = new_start
        

    def getIntervals(self) -> List[List[int]]:
        if self.result_cache != None:
            return self.result_cache

        result = []

        sorted_keys = sorted(self.start_to_end_mapping.keys())
        for key in sorted_keys:
            start = key
            end = self.start_to_end_mapping[key]
            result.append([start, end])

        
        self.result_cache = result
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
