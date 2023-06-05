#------------------------------------------------------
# Solution 1 - math
#------------------------------------------------------

# Runtime:  49.95%
# Memory:   51.67%


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # fot this, you'll need to know the equation for a line
        # y = mx + b

        # m = slope = rise / run = dy / dx = (y1 - y0) / (x1 - x0)

        # for line segments to be on the same line, they must
        # satisfy the same equation

        # one way to check this is to use the same point (base point?)
        # as one end of each line segment, then compare the slopes

        # same point + same slope = same ilne

        # So...

        # base point is p0 = x0, y0
        x0, y0 = coordinates[0]

        # first line segment to get the slope
        x1, y1 = coordinates[1]

        # slope = (y1 - y0) / (x1 - x0) #<-- BUT what if x1 - x0 == 0?  Div by zero is BAD...

        # so... let's see what else we can do...

        # we need two line segments that share p0
        # and we need the slopes to be the same

        # slope1 = (y1 - y0) / (x1 - x0)
        # slope2 = (y2 - y0) / (x2 - x0)

        # So...
        # slope1 == slop2 --> (y1 - y0) / (x1 - x0) == (y2 - y0) / (x2 - x0)
        #
        # We can refactor that by multiplyine each side by the other side's denominator
        #
        # (y1 - y0) * (x2 - x0) == (y2 - y0) * (x1 - x0)

        # MUCH better!

        rise = (y1 - y0)
        run = (x1 - x0)

        # now we just need to check all the other points!
        for x2, y2 in coordinates[2:]:
            if (x2 - x0) * rise != (y2 - y0) * run:
                return False

        return True