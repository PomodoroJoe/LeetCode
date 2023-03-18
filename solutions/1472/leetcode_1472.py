#------------------------------------------------------
# Solution 1
#------------------------------------------------------

# Runtime:  78.84%
# Memory:   96.29%


class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        self.current_index = 0
        self.max_index = 0
        

    def visit(self, url: str) -> None:
        self.current_index += 1

        if self.current_index >= len(self.data):
            self.data.append(url)
        else:
            self.data[self.current_index] = url

        self.max_index = self.current_index


    def back(self, steps: int) -> str:
        self.current_index = max(self.current_index - steps, 0)
        return self.data[self.current_index]


    def forward(self, steps: int) -> str:
        self.current_index = min(self.current_index + steps, self.max_index)
        return self.data[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



#------------------------------------------------------
# Solution 2 - min/max with if/else
#------------------------------------------------------

# Runtime:  84.55%
# Memory:   70.51%


class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        self.current_index = 0
        self.max_index = 0
        

    def visit(self, url: str) -> None:
        self.current_index += 1

        if self.current_index >= len(self.data):
            self.data.append(url)
        else:
            self.data[self.current_index] = url

        self.max_index = self.current_index


    def back(self, steps: int) -> str:
        if self.current_index - steps >= 0:
            self.current_index = self.current_index - steps
        else:
            self.current_index = 0

        return self.data[self.current_index]


    def forward(self, steps: int) -> str:
        if self.current_index + steps <= self.max_index:
            self.current_index = self.current_index + steps
        else:
            self.current_index = self.max_index

        return self.data[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



#------------------------------------------------------
# Solution 3 - min/max with pythonic if/else
#------------------------------------------------------

# Runtime:  93.13%
# Memory:   10.62%


class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        self.current_index = 0
        self.max_index = 0
        

    def visit(self, url: str) -> None:
        self.current_index += 1

        if self.current_index >= len(self.data):
            self.data.append(url)
        else:
            self.data[self.current_index] = url

        self.max_index = self.current_index


    def back(self, steps: int) -> str:
        self.current_index = self.current_index - steps if self.current_index - steps >= 0 else 0
        return self.data[self.current_index]


    def forward(self, steps: int) -> str:
        self.current_index = self.current_index + steps if self.current_index + steps <= self.max_index else self.max_index
        return self.data[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)



#------------------------------------------------------
# Solution 4 - min/max with pythonic if/else & short names
#------------------------------------------------------

# Runtime:  97.21%
# Memory:   37.32%


class BrowserHistory:

    def __init__(self, homepage: str):
        self.data = [homepage]
        self.index = 0
        self.max_index = 0
        

    def visit(self, url: str) -> None:
        self.index += 1

        if self.index >= len(self.data):
            self.data.append(url)
        else:
            self.data[self.index] = url

        self.max_index = self.index


    def back(self, steps: int) -> str:
        self.index = self.index - steps if self.index - steps > 0 else 0
        return self.data[self.index]


    def forward(self, steps: int) -> str:
        self.index = self.index + steps if self.index + steps < self.max_index else self.max_index
        return self.data[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)