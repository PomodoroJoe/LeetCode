#------------------------------------------------------
# Solution 1 - inverse dictionary
#------------------------------------------------------

# Runtime:  24.41%
# Memory:   41.20%


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        inverse = defaultdict(list)
        for num, freq in counts.items():
            inverse[freq].append(num)

        sorted_freq = sorted(inverse.keys(), reverse=True)

        index = 0
        result = []

        while len(result) < k:
            freq = sorted_freq[index]
            result += inverse[freq]
            index += 1

        return result[:k]



#------------------------------------------------------
# Solution 2 - list
#------------------------------------------------------

# Runtime:  88.14%
# Memory:   30.27%


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        freq_to_num = []
        for num, freq in counts.items():
            freq_to_num.append((freq, num))

        freq_to_num.sort(reverse=True)
        result = [e[1] for e in freq_to_num[:k]]

        return result



#------------------------------------------------------
# Solution 3 - Counter
#------------------------------------------------------

# Runtime:  43.78%
# Memory:   41.20%


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [e[0] for e in Counter(nums).most_common(k)]