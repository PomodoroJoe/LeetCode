#------------------------------------------------------
# Solution 1 - implicit set
#------------------------------------------------------

# Runtime:  92.58%
# Memory:   99.45%


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.replaced_nums = []


    def popSmallest(self) -> int:
        if self.replaced_nums:
            result = self.replaced_nums.pop(0)
            return result
            
        result = self.smallest
        self.smallest += 1

        return result
        

    def addBack(self, num: int) -> None:
        if num >= self.smallest:
            return

        if num not in self.replaced_nums:
            self.replaced_nums.append(num)
            self.replaced_nums.sort()
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)



#------------------------------------------------------
# Solution 2 - Solution 1 w/ minor change to addBack
#------------------------------------------------------

# Runtime:  87.64%
# Memory:   99.45%


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.replaced_nums = []


    def popSmallest(self) -> int:
        if self.replaced_nums:
            result = self.replaced_nums.pop(0)
            return result
            
        result = self.smallest
        self.smallest += 1

        return result
        

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            if num not in self.replaced_nums:
                self.replaced_nums.append(num)
                self.replaced_nums.sort()



#------------------------------------------------------
# Solution 3 - Solution 2 w/ improved addBack
#------------------------------------------------------

# Runtime: 100.00%
# Memory:   88.19%


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.replaced_nums = []


    def popSmallest(self) -> int:
        if self.replaced_nums:
            result = self.replaced_nums.pop(0)
            return result
            
        result = self.smallest
        self.smallest += 1

        return result
        

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.replaced_nums:
            self.replaced_nums.append(num)
            self.replaced_nums.sort()
