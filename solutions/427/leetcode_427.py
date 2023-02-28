#------------------------------------------------------
# Solution 1 - recursive
#------------------------------------------------------

# Runtime:  49.30%
# Memory:   06.65%


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def constructRecurse(x1, y1, x2, y2):
            if x1 == x2:
                return Node(val=grid[y1][x1], isLeaf=True)

            # Optimization: isLeaf?

            N = (x2 - x1) + 1
            half = N // 2

            TL = constructRecurse(x1       , y1       , x1 + half - 1, y1 + half - 1)
            TR = constructRecurse(x1 + half, y1       , x2           , y1 + half - 1)
            BL = constructRecurse(x1       , y1 + half, x1 + half - 1, y2)
            BR = constructRecurse(x1 + half, y1 + half, x2           , y2)

            total_val = sum([TL.val, TR.val, BL.val, BR.val])
            isLeaf = TL.isLeaf and TR.isLeaf and BL.isLeaf and BR.isLeaf

            node = Node()
            node.val = total_val // 4
            node.isLeaf = isLeaf and (total_val == 0 or total_val == 4)

            if node.isLeaf == False:
                node.topLeft = TL
                node.topRight = TR
                node.bottomLeft = BL
                node.bottomRight = BR

            return node

        grid_len = len(grid) - 1
        return constructRecurse(0, 0, grid_len, grid_len)



#------------------------------------------------------
# Solution 2 - recursive w/ early return
#------------------------------------------------------

# Runtime:  89.20%
# Memory:   20.22%


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def constructRecurse(x1, y1, x2, y2):
            if x1 == x2:
                return Node(val=grid[y1][x1], isLeaf=True)

            # Optimization: isLeaf?
            target_val = grid[y1][x1]
            isLeaf = True

            for i in range(y1, y2+1):
                for j in range(x1, x2+1):
                    if grid[i][j] != target_val:
                        isLeaf = False
                        break
                if not isLeaf:
                    break

            if isLeaf:
                return Node(val=target_val, isLeaf=True)

            N = (x2 - x1) + 1
            half = N // 2

            TL = constructRecurse(x1       , y1       , x1 + half - 1, y1 + half - 1)
            TR = constructRecurse(x1 + half, y1       , x2           , y1 + half - 1)
            BL = constructRecurse(x1       , y1 + half, x1 + half - 1, y2)
            BR = constructRecurse(x1 + half, y1 + half, x2           , y2)

            total_val = sum([TL.val, TR.val, BL.val, BR.val])
            isLeaf = TL.isLeaf and TR.isLeaf and BL.isLeaf and BR.isLeaf

            node = Node()
            node.val = total_val // 4
            node.isLeaf = isLeaf and (total_val == 0 or total_val == 4)

            if node.isLeaf == False:
                node.topLeft = TL
                node.topRight = TR
                node.bottomLeft = BL
                node.bottomRight = BR

            return node

        grid_len = len(grid) - 1
        return constructRecurse(0, 0, grid_len, grid_len)
