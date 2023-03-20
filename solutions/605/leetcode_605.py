#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  30.39%
# Memory:   94.10%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        for index, plot in enumerate(flowerbed):
            prev_plot = 0
            if index != 0:
                prev_plot = flowerbed[index - 1]

            next_plot = 0
            if index < len(flowerbed) - 1:
                next_plot = flowerbed[index + 1]

            if prev_plot == 0 and plot == 0 and next_plot == 0:
                count += 1
                flowerbed[index] = 1

        return count >= n



#------------------------------------------------------
# Solution 2 - early return
#------------------------------------------------------

# Runtime:  34.25%
# Memory:   65.78%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        for index, plot in enumerate(flowerbed):
            prev_plot = 0
            if index != 0:
                prev_plot = flowerbed[index - 1]

            next_plot = 0
            if index < len(flowerbed) - 1:
                next_plot = flowerbed[index + 1]

            if prev_plot == 0 and plot == 0 and next_plot == 0:
                count += 1
                flowerbed[index] = 1

                if count >= n:
                    return True

        return count >= n


#------------------------------------------------------
# Solution 3 - cascade plots (prev_prev, prev, plot)
#------------------------------------------------------

# Runtime:  92.51%
# Memory:   65.78%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        prev_prev = 0
        prev = flowerbed[0]

        for plot in flowerbed[1:]:
            if prev_prev == 0 and prev == 0 and plot == 0:
                count += 1
                prev = 1

            prev_prev = prev
            prev = plot

        if prev_prev == 0 and prev == 0:
            count += 1

        return count >= n


#------------------------------------------------------
# Solution 4 - cascade w/ early return
#------------------------------------------------------

# Runtime:  89.80%
# Memory:   65.78%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        prev_prev = 0
        prev = flowerbed[0]

        for plot in flowerbed[1:]:
            if prev_prev == 0 and prev == 0 and plot == 0:
                count += 1
                prev = 1

                if count >= n:
                    return True

            prev_prev = prev
            prev = plot

        if prev_prev == 0 and prev == 0:
            count += 1

        return count >= n


#------------------------------------------------------
# Solution 5 - cascade w/ zero compare (count)
#------------------------------------------------------

# Runtime:  95.54%
# Memory:   94.10%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = n

        prev_prev = 0
        prev = flowerbed[0]

        for plot in flowerbed[1:]:
            if prev_prev == 0 and prev == 0 and plot == 0:
                count -= 1
                prev = 1

                if count <= 0:
                    return True

            prev_prev = prev
            prev = plot

        if prev_prev == 0 and prev == 0:
            count -= 1

        return count <= 0


#------------------------------------------------------
# Solution 6 - cascade w/ sum
#------------------------------------------------------

# Runtime:  97.17%
# Memory:   20.94%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = n

        prev_prev = 0
        prev = flowerbed[0]

        for plot in flowerbed[1:]:
            if (prev_prev + prev + plot) == 0:
                count -= 1
                prev = 1

                if count <= 0:
                    return True

            prev_prev = prev
            prev = plot

        if prev_prev == 0 and prev == 0:
            count -= 1

        return count <= 0