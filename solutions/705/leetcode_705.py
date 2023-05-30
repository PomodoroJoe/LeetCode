#------------------------------------------------------
# Solution 1 - pre-allocated storage (array)
#------------------------------------------------------

# Runtime:  35.60%
# Memory:   05.23%


class MyHashSet:

    def __init__(self):
        self.storage = [0] * 1000001
        

    def add(self, key: int) -> None:
        self.storage[key] = 1
        

    def remove(self, key: int) -> None:
        self.storage[key] = 0


    def contains(self, key: int) -> bool:
        return self.storage[key] == 1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



#------------------------------------------------------
# Solution 2 - array w/ search
#------------------------------------------------------

# Runtime:  23.39%
# Memory:   45.60%


class MyHashSet:

    def __init__(self):
        self.storage = []
        

    def add(self, key: int) -> None:
        if key not in self.storage:
            self.storage.append(key)
        

    def remove(self, key: int) -> None:
        if key in self.storage:
            self.storage.remove(key)


    def contains(self, key: int) -> bool:
        return key in self.storage
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)



#------------------------------------------------------
# Solution 3 - buckets (array w/ bucket search)
#------------------------------------------------------

# Runtime:  54.27%
# Memory:   45.60%


class MyHashSet:

    def __init__(self):
        self.storage_size = 1000
        self.storage = [[] for _ in range(self.storage_size + 1)]
        
    
    def getKeys(self, key):
        bucket_key = key // self.storage_size
        secondary_key = key % self.storage_size
        return (bucket_key, secondary_key)


    def add(self, key: int) -> None:
        bucket_key, secondary_key = self.getKeys(key)
        bucket = self.storage[bucket_key]
        if secondary_key not in bucket:
            bucket.append(secondary_key)
        

    def remove(self, key: int) -> None:
        bucket_key, secondary_key = self.getKeys(key)
        bucket = self.storage[bucket_key]
        if secondary_key in bucket:
            bucket.remove(secondary_key)


    def contains(self, key: int) -> bool:
        bucket_key, secondary_key = self.getKeys(key)
        bucket = self.storage[bucket_key]
        return secondary_key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)