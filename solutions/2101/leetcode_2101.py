#------------------------------------------------------
# Solution 1 - graph traversal with DFS
#------------------------------------------------------

# Runtime:  80.29%
# Memory:    9.18%


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        result = 1

        bomb_count = len(bombs)
        bomb_edges = defaultdict(set)

        def distance_2(b1, b2):
            dx = b1[0] - b2[0]
            dy = b1[1] - b2[1]
            return (dx * dx) + (dy * dy)

        for i in range(bomb_count):
            source_bomb = bombs[i]
            for j in range(i+1, bomb_count):
                target_bomb = bombs[j]

                d_2 = distance_2(source_bomb, target_bomb)

                if d_2 <= pow(source_bomb[2], 2):
                    bomb_edges[i].add(j)

                if d_2 <= pow(target_bomb[2], 2):
                    bomb_edges[j].add(i)

        def dfs(start_index):
            stack = [start_index]
            visited = set([start_index])

            while stack:
                bomb_index = stack.pop(-1)

                for bomb in bomb_edges[bomb_index]:
                    if bomb in visited:
                        continue

                    stack.append(bomb)
                    visited.add(bomb)

            return len(visited)


        for i in range(bomb_count):
            chain_count = dfs(i)
            result = chain_count if chain_count > result else result

        return result