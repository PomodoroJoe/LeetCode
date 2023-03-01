#------------------------------------------------------
# Solution 1 - Merge Sort
#------------------------------------------------------

# Runtime:  24.10%
# Memory:   17.94%


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(a):
            if len(a) < 2:
                return a

            mid = len(a) // 2

            left = a[:mid]
            right = a[mid:]

            left = mergeSort(left)
            right = mergeSort(right)

            result = []

            # merge
            while left and right:
                if left[0] < right[0]:
                    val = left.pop(0)
                    result.append(val)
                else:
                    val = right.pop(0)
                    result.append(val)

            result = result + left + right

            return result

        return mergeSort(nums)



#------------------------------------------------------
# Solution 2 - Quick Sort
#------------------------------------------------------

# Runtime:  81.26%
# Memory:   21.89%


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(a):
            if len(a) < 2:
                return a

            mid = len(a) // 2

            left = a[:mid]
            right = a[mid:]

            left = mergeSort(left)
            right = mergeSort(right)

            result = []

            # merge
            while left and right:
                if left[0] < right[0]:
                    val = left.pop(0)
                    result.append(val)
                else:
                    val = right.pop(0)
                    result.append(val)

            result = result + left + right

            return result


        def quickSort(a):
            if len(a) < 2:
                return a

            pivot = random.choice(a)

            lower = []
            same = []
            higher = []

            for n in a:
                if n > pivot:
                    higher.append(n)
                elif n < pivot:
                    lower.append(n)
                else:
                    same.append(n)

            return quickSort(lower) + same + quickSort(higher)


        return quickSort(nums)