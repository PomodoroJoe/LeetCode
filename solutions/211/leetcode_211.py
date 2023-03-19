#------------------------------------------------------
# Solution 1 - trie
#------------------------------------------------------

# Runtime:  64.17%
# Memory:   84.48%


class WordDictionary:

    def __init__(self):
        # Trie, Tree
        # {'T'} --> {'r'} --> {'i', 'e'} --> {'e'} --> {'\0'}
        #                            \-----> {'e'} --> {'\0'}

        self.data = {}
        self.end_char = '\0'

    def addWord(self, word: str) -> None:
        data = self.data

        for c in word:
            if c not in data:
                data[c] = {}
            data = data[c]

        data[self.end_char] = {}
        

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.data)

    
    def searchHelper(self, word, data):
        if word and not data:
            return False

        if not word:
            return (self.end_char in data)
        
        for i, c in enumerate(word):
            if c == '.':
                for key in data:
                    if self.searchHelper(word[i+1:], data[key]):
                        return True
                return False
                continue

            if c not in data:
                return False
            data = data[c]

        return (self.end_char in data)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



#------------------------------------------------------
# Solution 2 - trie(s) by word length
#------------------------------------------------------

# Runtime:  99.89%
# Memory:   82.70%


class WordDictionary:

    def __init__(self):
        # Trie, Tree
        # {'T'} --> {'r'} --> {'i', 'e'} --> {'e'} --> {'\0'}
        #                            \-----> {'e'} --> {'\0'}

        self.datas = [{} for _ in range(26)]
        self.end_char = '\0'

    def addWord(self, word: str) -> None:
        data = self.datas[len(word)]

        for c in word:
            if c not in data:
                data[c] = {}
            data = data[c]

        data[self.end_char] = {}
        

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.datas[len(word)])

    
    def searchHelper(self, word, data):
        if word and not data:
            return False

        if not word:
            return (self.end_char in data)
        
        for i, c in enumerate(word):
            if c == '.':
                for key in data:
                    if self.searchHelper(word[i+1:], data[key]):
                        return True
                return False
                continue

            if c not in data:
                return False
            data = data[c]

        return (self.end_char in data)

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)