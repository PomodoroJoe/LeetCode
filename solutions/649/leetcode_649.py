#------------------------------------------------------
# Solution 1 - stack
#------------------------------------------------------

# Runtime:  81.35%
# Memory:    5.50%


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        result = None

        current_senate = senate

        done = False

        while not done:
            done = True

            next_senate = []
            stack = []

            # one round of voting
            for s in current_senate:
                if stack and stack[-1] != s:
                    ns = stack.pop(-1)
                    next_senate.append(ns)
                    
                    if next_senate[0] != ns:
                        done = False

                else:
                    stack.append(s)

            current_senate = stack + next_senate

            if stack and next_senate and stack[0] != next_senate[0]:
                done = False
            
        result = current_senate[0]
        return "Dire" if result == "D" else "Radiant"



#------------------------------------------------------
# Solution 2 - two queues
#------------------------------------------------------

# Runtime:  18.40%
# Memory:    5.50%


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_size = len(senate)

        r_indexes = []
        d_indexes = []

        for i, s in enumerate(senate):
            if s == "R":
                r_indexes.append(i)
            else:
                d_indexes.append(i)

        while r_indexes and d_indexes:
            r = r_indexes.pop(0)
            d = d_indexes.pop(0)

            if r < d:
                r_indexes.append(r + senate_size)
            else:
                d_indexes.append(d + senate_size)

        return "Dire" if d_indexes else "Radiant"



#------------------------------------------------------
# Solution 3 - Solution 2 w/ deque
#------------------------------------------------------

# Runtime:  62.39%
# Memory:    5.50%


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate_size = len(senate)

        r_indexes = deque()
        d_indexes = deque()

        for i, s in enumerate(senate):
            if s == "R":
                r_indexes.append(i)
            else:
                d_indexes.append(i)

        while r_indexes and d_indexes:
            r = r_indexes.popleft()
            d = d_indexes.popleft()

            if r < d:
                r_indexes.append(r + senate_size)
            else:
                d_indexes.append(d + senate_size)

        return "Dire" if d_indexes else "Radiant"