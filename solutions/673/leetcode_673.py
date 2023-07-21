#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  91.27%
# Memory:   78.54%


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        # Subsequence Problem
        #
        # Check each value in the array, and consider that value as
        # the END of some subsequence (made up of elements that came before this element)

        # Then we can track the LENGTH and the COUNTS of each potential subsequence.  Like this...

        result = 0


        # Track the Subsequences

        # the index corresponds to the index of the element in nums
        # lenghts = the longest subsequence that ends at this element (nums[index])
        # counts = the number of subsequences of lengths[index] that end at this element

        lengths = [1] * len(nums)   #<-- each element *could* be a subsequence of length 1
        counts = [1] * len(nums)    #<-- there's currently only 1 subsequence of len 1 that ends at
                                    #    each element

        for i in range(len(nums)):
            val = nums[i]

            # now check all of the elements that came before this one
            for j in range(i):
                if nums[j] < val:
                    # this is a strictly increasing subsequence
                    new_length = lengths[j] + 1 #<-- longest subsequence ending at nums[j] plus
                                                #    one more for this element at i

                    if new_length < lengths[i]:
                        # too short to be the longest... move on.
                        continue

                    if new_length == lengths[i]:
                        # same length as longest, just update the counts
                        counts[i] += counts[j]

                    if new_length > lengths[i]:
                        # new longest subsequence! reset lengths and counts
                        lengths[i] = new_length
                        counts[i] = counts[j]

        # done looping?  Figure the result...
        max_length = max(lengths)

        for i in range(len(lengths)):
            if lengths[i] == max_length:
                result += counts[i]

        return result