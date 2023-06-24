#------------------------------------------------------
# Solution 1 - dp
#------------------------------------------------------

# Runtime:  13.83%
# Memory:    6.18%


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        result = 2

        # dp = dictionary, key = (end_index, delta), value = len of subsequence
        # end_index = index that ends the subsequence
        # delta = the difference between elements in the subsequence
        # value = the length of the longest subsequence ending at end_index with spacing of delta

        dp = defaultdict(lambda: 1)

        for end_index in range(len(nums)):
            val = nums[end_index]

            for prev_index in range(end_index):
                prev_val = nums[prev_index]

                delta = val - prev_val

                lookup_key = (prev_index, delta)
                storage_key = (end_index, delta)

                prev_subsequence_count = dp[lookup_key]
                new_subsequence_count = 1 + prev_subsequence_count

                dp[storage_key] = new_subsequence_count

                result = max(result, new_subsequence_count)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/ set()
#------------------------------------------------------

# Runtime:  95.82%
# Memory:   54.00%


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        result = 2

        # dp = dictionary, key = (end_index, delta), value = len of subsequence
        # end_index = index that ends the subsequence
        # delta = the difference between elements in the subsequence
        # value = the length of the longest subsequence ending at end_index with spacing of delta

        dp = defaultdict(lambda: 1)

        prev_vals = set()

        for end_index in range(len(nums)):
            end_val = nums[end_index]

            for prev_val in prev_vals:

                delta = end_val - prev_val

                lookup_key = (prev_val, delta)
                storage_key = (end_val, delta)

                prev_subsequence_count = dp[lookup_key]
                new_subsequence_count = 1 + prev_subsequence_count

                dp[storage_key] = new_subsequence_count

                result = max(result, new_subsequence_count)

            prev_vals.add(end_val)

        return result