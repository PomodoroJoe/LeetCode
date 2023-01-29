
#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  61.38%
# Memory:   36.32%


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0

        self.cache_map = {}

        self.key_to_freq = defaultdict(int)
        self.freq_to_keys = defaultdict(OrderedDict)

        self.min_freq = 1
        

    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1

        self.update_key(key)
        return self.cache_map[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key] = value
            self.update_key(key)
            return

        # new k/v

        if self.count >= self.capacity:
            self.remove_lfu()

        if self.count < self.capacity:
            self.cache_map[key] = value
            self.update_key(key)
            self.count += 1
            self.min_freq = 1


    def update_key(self, key):
        # update count
        old_count = self.key_to_freq[key]
        new_count = old_count + 1

        self.key_to_freq[key] = new_count

        # update freq
        if old_count != 0:
            del self.freq_to_keys[old_count][key]
        self.freq_to_keys[new_count][key] = None

        if not self.freq_to_keys[old_count]:
            del self.freq_to_keys[old_count]

            if self.min_freq == old_count:
                self.min_freq = new_count


    def remove_lfu(self):
        if self.min_freq not in self.freq_to_keys:
            print("ERROR")
            return

        lfu_item = self.freq_to_keys[self.min_freq].popitem(0)
        lfu_key = lfu_item[0]

        # remove item from cache
        del self.cache_map[lfu_key]
        del self.key_to_freq[lfu_key]
        self.count -= 1

        # clean-up
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)