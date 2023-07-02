#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  50.48%
# Memory:   33.98%


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result = 0

        def is_valid_end_state(state):
            for balance in state:
                if balance != 0:
                    return False
            return True

        def maximumRequestsRecurse(request_index, state, count):
            result = 0

            if is_valid_end_state(state):
                result = count
                count = 0

            if request_index >= len(requests):
                return result

            # DON'T do the request
            option_1 = maximumRequestsRecurse(request_index + 1, state, count)

            # DO the request
            request_from, request_to = requests[request_index]

            new_state = state.copy()
            new_state[request_from] -= 1
            new_state[request_to] += 1

            option_2 = maximumRequestsRecurse(request_index + 1, new_state, count + 1)

            return result + max(option_1, option_2)


        state = [0] * n
        result = maximumRequestsRecurse(0, state, 0)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ global state
#------------------------------------------------------

# Runtime:  49.51%
# Memory:   53.40%


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        result = 0

        def is_valid_end_state(state):
            for balance in state:
                if balance != 0:
                    return False
            return True

        global_state = [0] * n

        def maximumRequestsRecurse(request_index, count):
            result = 0

            if is_valid_end_state(global_state):
                result = count
                count = 0

            if request_index >= len(requests):
                return result

            # DON'T do the request
            option_1 = maximumRequestsRecurse(request_index + 1, count)

            # DO the request
            request_from, request_to = requests[request_index]

            global_state[request_from] -= 1
            global_state[request_to] += 1

            option_2 = maximumRequestsRecurse(request_index + 1, count + 1)

            global_state[request_from] += 1
            global_state[request_to] -= 1

            return result + max(option_1, option_2)


        result = maximumRequestsRecurse(0, 0)

        return result