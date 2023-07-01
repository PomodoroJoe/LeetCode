#------------------------------------------------------
# Solution 1 - union find (kinda)
#------------------------------------------------------

# Runtime:  89.67%
# Memory:   59.78%


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        result = 0

        # key = cell (r, c), value = group label (r, c)
        cell_to_group_map = {}

        # key = group, value set of columns
        group_to_col_map = {}

        def find(cell):
            if cell in cell_to_group_map:
                return cell_to_group_map[cell]
            cell_to_group_map[cell] = cell
            group_to_col_map[cell] = set([cell[1]])
            return cell

        def union(cell_01, cell_02):
            group_01 = find(cell_01)
            group_02 = find(cell_02)

            if group_01 == group_02:
                return

            if group_to_col_map[group_02]:
                group_02_columns = group_to_col_map[group_02]
                group_to_col_map[group_01] = group_to_col_map[group_01].union(group_02_columns)
                group_to_col_map[group_02] = None

            cell_to_group_map[cell_02] = group_01
            union(cell_01, group_02)

        
        def is_complete(coords):
            group = find(coords)
            cols = group_to_col_map[group]

            return len(cols) == col


        for day, cell in enumerate(cells):
            coords = tuple(cell)

            find(coords)

            offsets = [
                (-1, -1), (0, -1), (1, -1), \
                (-1,  0),          (1,  0), \
                (-1,  1), (0,  1), (1,  1)  \
            ]

            r, c = coords

            for o in offsets:
                neighbor = (r + o[0], c + o[1])

                if neighbor[0] < 1 or neighbor[1] < 0 or neighbor[0] > row or neighbor[1] > col:
                    continue

                if neighbor in cell_to_group_map:
                    union(coords, neighbor)

                    if is_complete(coords):
                        return day

        return result