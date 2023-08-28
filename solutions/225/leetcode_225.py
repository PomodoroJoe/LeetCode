#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  90.94%
# Memory:   67.60%


class MyStack:

    def __init__(self):
        self.storage = []
        

    def push(self, x: int) -> None:
        self.storage.append(x)


    def pop(self) -> int:
        temp_storage = []
        for x in range(len(self.storage) - 1):
            temp_storage.append(self.storage.pop(0))
        
        result = self.storage.pop(0)
        self.storage = temp_storage

        return result


    def top(self) -> int:
        result = self.pop()
        self.push(result)
        return result
        

    def empty(self) -> bool:
        return len(self.storage) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()