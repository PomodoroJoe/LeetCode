#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  74.33%
# Memory:   91.52%


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []

        groups = defaultdict(list)

        for person_id, group_id in enumerate(groupSizes):
            groups[group_id].append(person_id)
            if len(groups[group_id]) == group_id:
                result.append(groups[group_id])
                groups[group_id] = []

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ short names
#------------------------------------------------------

# Runtime:  82.82%
# Memory:   64.84%


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []

        groups = defaultdict(list)

        for i, s in enumerate(groupSizes):
            groups[s].append(i)
            if len(groups[s]) == s:
                result.append(groups[s])
                groups[s] = []

        return result



#------------------------------------------------------
# Solution 3 - Solution 2 w/ del
#------------------------------------------------------

# Runtime:  87.50%
# Memory:   64.84%


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []

        groups = defaultdict(list)

        for i, s in enumerate(groupSizes):
            groups[s].append(i)
            if len(groups[s]) == s:
                result.append(groups[s])
                del groups[s]

        return result    