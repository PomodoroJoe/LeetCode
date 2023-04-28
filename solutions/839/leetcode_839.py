#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  19.87%
# Memory:   10.26%


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        result = 0

        group = [None] * len(strs)

        def areSimilar(w1, w2):
            if w1 == w2:
                return True

            non_matching_indexes = []
            
            for i, c in enumerate(w1):
                if c != w2[i]:
                    non_matching_indexes.append(i)

            if len(non_matching_indexes) != 2:
                return False

            i1 = non_matching_indexes[0]
            i2 = non_matching_indexes[1]

            return w1[i2] == w2[i1] and w1[i1] == w2[i2]


        def merge_groups(g1, g2):
            common_label = min(g1, g2)

            for i in range(len(group)):
                if group[i] == g1 or group[i] == g2:
                    group[i] = common_label


        for i, word in enumerate(strs):
            if group[i] == None:
                result += 1
                group[i] = result

            for j in range(i+1, len(strs)):
                if areSimilar(word, strs[j]):
                    if group[j] == None:
                        group[j] = group[i]
                        continue

                    if group[i] != group[j]:
                        merge_groups(group[i], group[j])

        result = set(group)
        return len(result)