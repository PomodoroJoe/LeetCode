#------------------------------------------------------
# Solution 1 - BFS
#------------------------------------------------------

# Runtime:  59.68%
# Memory:   93.33%


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        result = -1

        start = None

        keys = set()
        locks = set()

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        # find start
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                val = grid[y][x]

                if val == "@":
                    start = (x, y)
                elif val in "abcdef":
                    keys.add(val)
                elif val in "ABCDEF":
                    locks.add(val)

        # (pos, inventory, steps)
        queue = [(start, "", 0)]

        # visited: key = inventory_state, value = set of visited cells
        visited = defaultdict(set)

        def add_key_to_inventory(inventory, k):
            inventory += k
            inventory = ''.join(sorted(list(inventory)))
            return inventory

        def can_unlock(cell_val, inventory):
            return cell_val.lower() in inventory

        while queue:
            state = queue.pop(0)

            pos = state[0]
            inventory = state[1]
            steps = state[2]

            x, y = pos

            val = grid[y][x]

            if val in keys:
                if val not in inventory:
                    inventory = add_key_to_inventory(inventory, val)

                    if len(inventory) == len(keys):
                        return steps

                    visited[inventory] = set(pos)

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            for d in directions:
                if d == None or d in visited[inventory]:
                    continue

                dx, dy = d

                cell_val = grid[dy][dx]

                if cell_val == '#':
                    continue

                if cell_val in locks:
                    if not can_unlock(cell_val, inventory):
                        continue

                queue.append((d, inventory, steps + 1))
                visited[inventory].add(d)

        return result




#------------------------------------------------------
# Solution 2- Solution 1 w/ deque
#------------------------------------------------------

# Runtime:  66.30%
# Memory:   95.87%


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        result = -1

        start = None

        keys = set()
        locks = set()

        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1

        # find start
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                val = grid[y][x]

                if val == "@":
                    start = (x, y)
                elif val in "abcdef":
                    keys.add(val)
                elif val in "ABCDEF":
                    locks.add(val)

        # (pos, inventory, steps)
        queue = deque([(start, "", 0)])

        # visited: key = inventory_state, value = set of visited cells
        visited = defaultdict(set)

        def add_key_to_inventory(inventory, k):
            inventory += k
            inventory = ''.join(sorted(list(inventory)))
            return inventory

        def can_unlock(cell_val, inventory):
            return cell_val.lower() in inventory

        while queue:
            state = queue.popleft()

            pos = state[0]
            inventory = state[1]
            steps = state[2]

            x, y = pos

            val = grid[y][x]

            if val in keys:
                if val not in inventory:
                    inventory = add_key_to_inventory(inventory, val)

                    if len(inventory) == len(keys):
                        return steps

                    visited[inventory] = set(pos)

            up = (x, y - 1) if y > 0 else None
            dn = (x, y + 1) if y < max_y else None
            lt = (x - 1, y) if x > 0 else None
            rt = (x + 1, y) if x < max_x else None

            directions = [up, dn, lt, rt]

            for d in directions:
                if d == None or d in visited[inventory]:
                    continue

                dx, dy = d

                cell_val = grid[dy][dx]

                if cell_val == '#':
                    continue

                if cell_val in locks:
                    if not can_unlock(cell_val, inventory):
                        continue

                queue.append((d, inventory, steps + 1))
                visited[inventory].add(d)

        return result