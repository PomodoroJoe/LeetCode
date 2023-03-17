#------------------------------------------------------
# Solution 1 - dictionaries
#------------------------------------------------------

# Runtime:  95.91%
# Memory:   85.40%


class Trie:

    def __init__(self):
        self.data = {}
        self.end_char = '\0'

    def insert(self, word: str) -> None:
        data = self.data
        for c in word:
            if c not in data:
                data[c] = {}
            data = data[c]
        
        data[self.end_char] = {}
        

    def search(self, word: str) -> bool:
        data = self.data

        for c in word:
            if c not in data:
                return False
            data = data[c]

        return (self.end_char in data)
        

    def startsWith(self, prefix: str) -> bool:
        data = self.data

        for c in prefix:
            if c not in data:
                return False
            data = data[c]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)