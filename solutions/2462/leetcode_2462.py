
#------------------------------------------------------
# Solution 1 - heap
#------------------------------------------------------

# Runtime:  14.17%
# Memory:    6.17%


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        result = 0

        left_index = candidates
        right_index = len(costs) - 1 - candidates

        heap = []
        visited = set()

        for i in range(candidates):
            left_worker = (costs[i], i)

            if left_worker not in visited:
                heap.append(left_worker)
                visited.add(left_worker)

            j = len(costs) - 1 - i
            right_worker = (costs[j], j)
            if right_worker not in visited:
                heap.append(right_worker)
                visited.add(right_worker)

        # heapq
        # heapq.push
        # heapq.pop
        # heapq.heapify

        heapq.heapify(heap)
        worker_count = 0

        while worker_count < k:
            worker = heapq.heappop(heap)
            worker_count += 1

            result += worker[0]

            if left_index > right_index:
                continue

            if worker[1] < left_index:
                new_worker = (costs[left_index], left_index)
                heapq.heappush(heap, new_worker)
                left_index += 1
                continue

            if worker[1] > right_index:
                new_worker = (costs[right_index], right_index)
                heapq.heappush(heap, new_worker)
                right_index -= 1

        return result