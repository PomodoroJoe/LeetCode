#------------------------------------------------------
# Solution 1 - stack
#------------------------------------------------------

# Runtime:  28.29%
# Memory:   57.73%


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        #   A       B
        #  <--     <--      NO PROBLEM!!! :)
        #  <--     -->      NO PROBLEM!!! :)
        #  -->     <--      PROBLEM! KABOOM!!!
        #  -->     -->      NO PROBLEM!!! :)

        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            A = stack[-1]
            B = asteroid

            A_moving_left = A < 0
            B_moving_left = B < 0

            if A_moving_left == B_moving_left:
                stack.append(asteroid)
                continue
        
            if A_moving_left and not B_moving_left:
                stack.append(asteroid)
                continue

            B_size = -B

            while stack and stack[-1] > 0 and B:
                A = stack[-1]
                A_size = A

                if A_size > B_size:
                    # B asteroid is exploded!
                    B = None
                    continue

                if A_size == B_size:
                    # Both are exploded!
                    A = None
                    B = None
                    stack.pop(-1)
                    continue

                stack.pop(-1)
                

            if B:
                stack.append(B)

        return stack



#------------------------------------------------------
# Solution 2 - Solution 1 (cleaned-up)
#------------------------------------------------------

# Runtime:  66.59%
# Memory:   25.63%


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        #   A       B
        #  <--     <--      NO PROBLEM!!! :)
        #  <--     -->      NO PROBLEM!!! :)
        #  -->     <--      PROBLEM! KABOOM!!!
        #  -->     -->      NO PROBLEM!!! :)

        stack = []

        for B in asteroids:
            if not stack:
                stack.append(B)
                continue

            A_moving_left = stack[-1] < 0
            B_moving_left = B < 0

            if A_moving_left == B_moving_left:
                stack.append(B)
                continue
        
            if A_moving_left and not B_moving_left:
                stack.append(B)
                continue

            B_size = -B

            while stack and stack[-1] > 0 and B:
                A = stack[-1]
                A_size = A

                if A_size > B_size:
                    B = None
                    continue

                if A_size == B_size:
                    A = None
                    B = None
                    stack.pop(-1)
                    continue

                stack.pop(-1)
                

            if B:
                stack.append(B)

        return stack