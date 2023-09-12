#------------------------------------------------------
# Solution 1 - queue (BFS)
#------------------------------------------------------

# Runtime:  41.68%
# Memory:   93.71%


class Solution:
    def minDeletions(self, s: str) -> int:
        result = 0

        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1

        queue = []

        freq_to_count_map = defaultdict(int)
        for key, value in freqs.items():
            freq_to_count_map[value] += 1
            if freq_to_count_map[value] > 1:
                queue.append(value)

        while queue:
            freq = queue.pop(0)

            result += 1
            new_freq = freq - 1

            freq_to_count_map[new_freq] += 1
            if new_freq != 0 and freq_to_count_map[new_freq] > 1:
                queue.append(new_freq)

        return result



#------------------------------------------------------
# Solution 2 - Solution 1 w/o helper vars
#------------------------------------------------------

# Runtime:  46.57%
# Memory:   93.71%


class Solution:
    def minDeletions(self, s: str) -> int:
        result = 0

        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1

        queue = []

        freq_to_count_map = defaultdict(int)
        for key, value in freqs.items():
            freq_to_count_map[value] += 1
            if freq_to_count_map[value] > 1:
                queue.append(value)

        while queue:
            freq = queue.pop(0)

            result += 1
            freq -= 1

            freq_to_count_map[freq] += 1
            if freq != 0 and freq_to_count_map[freq] > 1:
                queue.append(freq)

        return result


#------------------------------------------------------
# Solution 3 - Solution 2 (DFS)
#------------------------------------------------------

# Runtime:  51.50%
# Memory:   23.36%


class Solution:
    def minDeletions(self, s: str) -> int:
        result = 0

        freqs = defaultdict(int)
        for c in s:
            freqs[c] += 1

        queue = []

        freq_to_count_map = defaultdict(int)
        for key, value in freqs.items():
            freq_to_count_map[value] += 1
            if freq_to_count_map[value] > 1:
                queue.append(value)

        while queue:
            freq = queue.pop(-1)

            result += 1
            freq -= 1

            freq_to_count_map[freq] += 1
            if freq != 0 and freq_to_count_map[freq] > 1:
                queue.append(freq)

        return result