#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  44.81%
# Memory:   15.56%

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        result = -1

        n = len(board)
        end_pos = (n * n)

        needs_flip = False
        flat_board = []

        for row in board[::-1]:
            new_row = row.copy()
            if needs_flip:
                new_row = new_row[::-1]
            flat_board.extend(new_row)
            needs_flip = not needs_flip

        def find_destination(pos):
            if pos >= end_pos:
                return end_pos

            index = pos - 1
            return flat_board[index] if flat_board[index] != -1 else pos

        visited = set()
        stack = [(1, 0)]

        while stack:
            pos, moves = stack.pop(0)

            if pos == end_pos:
                if result == -1:
                    result = moves
                result = min(result, moves)
                continue

            if pos in visited:
                continue

            visited.add(pos)

            for i in range(1, 7):
                next_pos = find_destination(pos + i)
                stack.append((next_pos, moves + 1))

        return result
