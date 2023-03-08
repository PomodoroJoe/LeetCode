#------------------------------------------------------
# Solution 1 - binary search
#------------------------------------------------------

# Runtime:  88.40%
# Memory:   16.17%


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # hmm... let's do a binary search

        lower_bound = 1             # <-- bananas / hour
        upper_bound = max(piles)    # <-- " " (this is probably too high)

        # let's make a helper function here

        def canEatAll(K):   # <-- K == bananas / hour
            totalTime = 0

            for pile in piles:
                totalTime += ceil(pile / K) # <-- need the cieling here
                if totalTime > h:
                    return False

            return totalTime <= h


        # NOW let's do a binary search

        while upper_bound >= lower_bound:
            mid = lower_bound + ((upper_bound - lower_bound) // 2)

            canEatAllBananas = canEatAll(mid)

            if canEatAllBananas:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return lower_bound



#------------------------------------------------------
# Solution 2 - binary search w/ better lower bound
#------------------------------------------------------

# Runtime:  88.67%
# Memory:   62.86%


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # hmm... let's do a binary search

        lower_bound = ceil(sum(piles) / h)  # <-- bananas / hour
        upper_bound = max(piles)            # <-- " " (this is probably too high)

        # let's make a helper function here

        def canEatAll(K):   # <-- K == bananas / hour
            totalTime = 0

            for pile in piles:
                totalTime += ceil(pile / K) # <-- need the cieling here
                if totalTime > h:
                    return False

            return totalTime <= h


        # NOW let's do a binary search

        while upper_bound >= lower_bound:
            mid = lower_bound + ((upper_bound - lower_bound) // 2)

            canEatAllBananas = canEatAll(mid)

            if canEatAllBananas:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return lower_bound



#------------------------------------------------------
# Solution 3 - binary search w/ better upper bound
#------------------------------------------------------

# Runtime:  99.78%
# Memory:   62.86%


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # hmm... let's do a binary search

        lower_bound = ceil(sum(piles) / h)  # <-- bananas / hour

        hours_per_pile = h // len(piles)
        upper_bound = ceil(max(piles) / hours_per_pile) # <-- better?

        # let's make a helper function here

        def canEatAll(K):   # <-- K == bananas / hour
            totalTime = 0

            for pile in piles:
                totalTime += ceil(pile / K) # <-- need the cieling here
                if totalTime > h:
                    return False

            return totalTime <= h


        # NOW let's do a binary search

        while upper_bound >= lower_bound:
            mid = lower_bound + ((upper_bound - lower_bound) // 2)

            canEatAllBananas = canEatAll(mid)

            if canEatAllBananas:
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1

        return lower_bound