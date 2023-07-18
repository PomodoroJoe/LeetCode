#------------------------------------------------------
# Solution 1 - OrderedDict
#------------------------------------------------------

# Runtime:  95.90%
# Memory:   86.71%


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.storage:
            self.storage.move_to_end(key, False)
            return self.storage[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.storage:
            self.storage.move_to_end(key, False)
            self.storage[key] = value
            return

        if len(self.storage) >= self.capacity:
            self.storage.popitem()

        self.storage[key] = value
        self.storage.move_to_end(key, False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)