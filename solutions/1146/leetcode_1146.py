
#------------------------------------------------------
# Solution 1 - full snapshot storage
#------------------------------------------------------

# MEMORY LIMIT EXCEEDED

# Runtime:  N/A
# Memory:   N/A


class SnapshotArray:

    def __init__(self, length: int):
        self.data = {}
        self.snapshots = []
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        

    def snap(self) -> int:
        self.snapshots.append(self.data.copy())
        self.snap_id +=1

        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index] if index in self.snapshots[snap_id] else 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)



#------------------------------------------------------
# Solution 2 - snapshot delta storage w/ linear search
#------------------------------------------------------

# MEMORY LIMIT EXCEEDED

# Runtime:   8.35%
# Memory:   78.71%


class SnapshotArray:

    def __init__(self, length: int):
        # key = index, val = val
        self.data = {}

        # index = index, val = [] of (snap_id, val)
        self.snapshots = [[] for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        

    def snap(self) -> int:
        for index in self.data:
            self.snapshots[index].append((self.snap_id, self.data[index]))
        
        self.snap_id +=1
        self.data = {}
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        result = 0
        snapshots = self.snapshots[index]

        for snap, val in snapshots:
            if snap <= snap_id:
                result = val
            else:
                break

        return result




#------------------------------------------------------
# Solution 3 - snapshot delta storage w/ binary search
#------------------------------------------------------

# MEMORY LIMIT EXCEEDED

# Runtime:  89.80%
# Memory:   80.19%


class SnapshotArray:

    def __init__(self, length: int):
        # key = index, val = val
        self.data = {}

        # index = index, val = [] of (snap_id, val)
        self.snapshots = [[] for _ in range(length)]
        self.snap_id = 0
        

    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        

    def snap(self) -> int:
        for index in self.data:
            self.snapshots[index].append((self.snap_id, self.data[index]))
        
        self.snap_id +=1
        self.data = {}
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        result = 0
        snapshots = self.snapshots[index]

        snap = bisect.bisect_right(snapshots, snap_id, key=lambda x: x[0])
        result = snapshots[snap - 1][1] if snap > 0 else 0

        return result