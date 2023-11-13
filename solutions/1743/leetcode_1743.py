#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  92.14%
# Memory:   33.70%


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        result = []

        adjacentTo = defaultdict(set)
        for n1, n2 in adjacentPairs:
            adjacentTo[n1].add(n2)
            adjacentTo[n2].add(n1)

        # find end points
        end_point = None
        for k, v in adjacentTo.items():
            if len(v) == 1:
                end_point = k
                break

        val = end_point
        prev_val = None

        while val != None:
            result.append(val)

            next_val = None
            for node in adjacentTo[val]:
                if node != prev_val:
                    next_val = node
                    break
            
            prev_val = val
            val = next_val

        return result