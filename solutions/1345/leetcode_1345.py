#------------------------------------------------------
# Solution 1 - graph traversal
#------------------------------------------------------

# TIME LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        result = inf

        edges = defaultdict(list)

        for i, val in enumerate(arr):
            edges[val].append(i)

        arr_len = len(arr)
        last_step = arr_len - 1

        result_arr = [inf] * arr_len
        result_arr[0] = 0

        queue = [0]
        while queue:
            step = queue.pop(0)

            if step == last_step:
                return result_arr[-1]

            step_count = result_arr[step]
            next_step_count = step_count + 1

            jump_id = arr[step]

            connected_steps = edges[jump_id]
            connected_steps += [step - 1, step + 1]

            for connected_step in connected_steps:
                if connected_step == step or connected_step < 0 or connected_step > last_step:
                    continue
                
                if result_arr[connected_step] > next_step_count:
                    result_arr[connected_step] = next_step_count
                    queue.append(connected_step)
            
        return result_arr[-1]



#------------------------------------------------------
# Solution 2 - limited graph traversal
#------------------------------------------------------

# Runtime:  10.31%
# Memory:   97.87%


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        result = inf

        edges = defaultdict(list)

        for i, val in enumerate(arr):
            edges[val].append(i)

        arr_len = len(arr)
        last_step = arr_len - 1

        result_arr = [inf] * arr_len
        result_arr[0] = 0

        queue = [0]
        while queue:
            step = queue.pop(0)

            if step == last_step:
                return result_arr[-1]

            step_count = result_arr[step]
            next_step_count = step_count + 1

            jump_id = arr[step]

            connected_steps = edges[jump_id]
            connected_steps += [step - 1, step + 1]

            for connected_step in connected_steps:
                if connected_step == step or connected_step < 0 or connected_step > last_step:
                    continue
                
                if result_arr[connected_step] > next_step_count:
                    result_arr[connected_step] = next_step_count
                    queue.append(connected_step)

            edges[jump_id] = []
            
        return result_arr[-1]



#------------------------------------------------------
# Solution 3 - limited graph traversal w/ early return
#------------------------------------------------------

# Runtime:  11.29%
# Memory:   98.35%


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        result = inf

        edges = defaultdict(list)

        for i, val in enumerate(arr):
            edges[val].append(i)

        arr_len = len(arr)
        last_step = arr_len - 1

        result_arr = [inf] * arr_len
        result_arr[0] = 0

        queue = [0]
        while queue:
            step = queue.pop(0)

            if step == last_step:
                return result_arr[-1]

            step_count = result_arr[step]
            next_step_count = step_count + 1

            if step_count >= result_arr[-1]:
                continue

            jump_id = arr[step]

            connected_steps = edges[jump_id]
            connected_steps += [step - 1, step + 1]

            for connected_step in connected_steps:
                if connected_step == step or connected_step < 0 or connected_step > last_step:
                    continue
                
                if result_arr[connected_step] > next_step_count:
                    result_arr[connected_step] = next_step_count
                    queue.append(connected_step)

            edges[jump_id] = []
            
        return result_arr[-1]



#------------------------------------------------------
# Solution 4 - imited graph traversal w/ duque
#------------------------------------------------------

# Runtime:  73.46%
# Memory:   97.50%


from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        result = inf

        edges = defaultdict(list)

        for i, val in enumerate(arr):
            edges[val].append(i)

        arr_len = len(arr)
        last_step = arr_len - 1

        result_arr = [inf] * arr_len
        result_arr[0] = 0

        queue = deque([0])

        while queue:
            step = queue.popleft()

            if step == last_step:
                return result_arr[-1]

            step_count = result_arr[step]
            next_step_count = step_count + 1

            if step_count >= result_arr[-1]:
                continue

            jump_id = arr[step]

            connected_steps = edges[jump_id]
            connected_steps += [step - 1, step + 1]

            for connected_step in connected_steps:
                if connected_step == step or connected_step < 0 or connected_step > last_step:
                    continue
                
                if result_arr[connected_step] > next_step_count:
                    result_arr[connected_step] = next_step_count
                    queue.append(connected_step)

            edges[jump_id] = []
            
        return result_arr[-1]