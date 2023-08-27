#------------------------------------------------------
# Solution 1 - BFS
#------------------------------------------------------

# Runtime:  48.96%
# Memory:   62.91%


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stone_map = defaultdict(bool)
        for stone in stones:
            stone_map[stone] = True

        # (pos, k)
        queue = [(0, 0)]
        visited = set()

        while queue:
            state = queue.pop(0)

            if state in visited:
                continue

            visited.add(state)

            pos, k = state

            if pos == stones[-1]:
                return True

            if pos > stones[-1]:
                continue

            # option 1 = k - 1
            new_k = k - 1
            new_pos = pos + new_k
            if new_pos > pos and stone_map[new_pos]:
                queue.append((new_pos, new_k))

            # option 2 = k
            new_k = k
            new_pos = pos + new_k
            if new_pos > pos and stone_map[new_pos]:
                queue.append((new_pos, new_k))

            # option 3 = k + 1
            new_k = k + 1
            new_pos = pos + new_k
            if new_pos > pos and stone_map[new_pos]:
                queue.append((new_pos, new_k))


        return False



#------------------------------------------------------
# Solution 4 - Solution 1 w/ set & loop
#------------------------------------------------------

# Runtime:  47.56%
# Memory:   65.96%


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stone_map = set(stones)

        # (pos, k)
        queue = [(0, 0)]
        visited = set()

        while queue:
            state = queue.pop(0)

            if state in visited:
                continue

            visited.add(state)

            pos, k = state
            if pos > stones[-1]:
                continue
                
            if pos == stones[-1]:
                return True

            # option 1 = k - 1
            offsets = [-1, 0, 1]
            for offset in offsets:
                new_k = k + offset
                new_pos = pos + new_k
                if new_pos > pos and new_pos in stone_map:
                    queue.append((new_pos, new_k))

        return False



#------------------------------------------------------
# Solution 5 - Solution 4 w/ DFS
#------------------------------------------------------

# Runtime:  96.65%
# Memory:   71.75%


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stone_map = set(stones)

        # (pos, k)
        queue = [(0, 0)]
        visited = set()

        while queue:
            state = queue.pop(-1)

            if state in visited:
                continue
            visited.add(state)

            pos, k = state
            if pos > stones[-1]:
                continue

            if pos == stones[-1]:
                return True

            # option 1 = k - 1
            offsets = [-1, 0, 1]
            for offset in offsets:
                new_k = k + offset
                new_pos = pos + new_k
                if new_pos > pos and new_pos in stone_map:
                    queue.append((new_pos, new_k))

        return False
