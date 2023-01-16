#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  86.85%
# Memory:   91.20%

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        index = 0

        # before
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        # overlapping
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1

        result.append(newInterval)

        # after
        while index < len(intervals):
            result.append(intervals[index])
            index += 1

        return result



#------------------------------------------------------
# Solution 2 - in-place
#------------------------------------------------------

# Runtime:  54.00%
# Memory:   51.90%

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # find overlapping intervals
        overlappingIntervals = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                continue

            if interval[0] > newInterval[1]:
                break

            overlappingIntervals.append(interval)

        # merge and remove intervals
        for interval in overlappingIntervals:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])

            intervals.remove(interval)

        # find insertion index
        insertionIndex = 0
        for index, interval in enumerate(intervals):
            if interval[0] < newInterval[0]:
                insertionIndex = index + 1

        intervals.insert(insertionIndex, newInterval)

        return intervals 



#------------------------------------------------------
# Solution 3 - in-place w/ insertion index early out
#------------------------------------------------------

# Runtime:  47.30%
# Memory:   91.20%

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # find overlapping intervals
        overlappingIntervals = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                continue

            if interval[0] > newInterval[1]:
                break

            overlappingIntervals.append(interval)

        # merge and remove intervals
        for interval in overlappingIntervals:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])

            intervals.remove(interval)

        # find insertion index
        insertionIndex = 0
        for index, interval in enumerate(intervals):
            if interval[0] < newInterval[0]:
                insertionIndex = index + 1
                continue
            break

        intervals.insert(insertionIndex, newInterval)

        return intervals 




#------------------------------------------------------
# Solution 4 - in-place w/ early insertion index
#------------------------------------------------------

# Runtime:  61.50%
# Memory:   91.20%

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # find overlapping intervals and insertion index
        insertionIndex = 0
        overlappingIntervals = []
        for index, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                insertionIndex = index + 1
                continue

            if interval[0] > newInterval[1]:
                break

            overlappingIntervals.append(interval)

        # merge and remove intervals
        for interval in overlappingIntervals:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])

            intervals.remove(interval)

        intervals.insert(insertionIndex, newInterval)

        return intervals 
