#------------------------------------------------------
# Solution 1 - brute force
#------------------------------------------------------

# MEMORY LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        for n1 in nums1:
            for n2 in nums2:
                result.append((n1, n2))

        result.sort(key = lambda x: sum(x))
        return result[:k]



#------------------------------------------------------
# Solution 2 - heap
#------------------------------------------------------

# Runtime:  34.89%
# Memory:   45.85%


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []

        max_index_1 = len(nums1) - 1
        max_index_2 = len(nums2) - 1

        # heap values = (sum, (n1, n2))

        first_pair = (0, 0)
        heap = [(nums1[0] + nums2[0], first_pair)]
        count = 0

        visited = set((0, 0))

        while heap and count < k:
            val, (i1, i2) = heapq.heappop(heap)

            result.append([nums1[i1], nums2[i2]])
            count += 1

            new_i1 = i1 + 1
            if new_i1 <= max_index_1:
                new_val = nums1[new_i1] + nums2[i2]
                new_element = (new_val, (new_i1, i2))

                if new_element not in visited:
                    heapq.heappush(heap, new_element)
                    visited.add(new_element)

            new_i2 = i2 + 1
            if new_i2 <= max_index_2:
                new_val = nums1[i1] + nums2[new_i2]
                new_element = (new_val, (i1, new_i2))
                
                if new_element not in visited:
                    heapq.heappush(heap, new_element)
                    visited.add(new_element)

        return result