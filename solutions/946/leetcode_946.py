#------------------------------------------------------
# Solution 1 - stack w/ list
#------------------------------------------------------

# Runtime:  36.36%
# Memory:   85.31%


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0

        for n in pushed:
            stack.append(n)

            while stack and popped[pop_index] == stack[-1]:
                stack.pop(-1)
                pop_index += 1

        return True if pop_index == len(popped) else False



#------------------------------------------------------
# Solution 3 - stack w/ deque
#------------------------------------------------------

# Runtime:  97.76%
# Memory:   34.41%


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        pop_index = 0

        for n in pushed:
            stack.append(n)

            while stack and popped[pop_index] == stack[-1]:
                stack.pop()
                pop_index += 1

        return True if pop_index == len(popped) else False
