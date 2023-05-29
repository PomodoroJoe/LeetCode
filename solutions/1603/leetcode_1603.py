#------------------------------------------------------
# Solution 1 - array
#------------------------------------------------------

# Runtime:  91.61%
# Memory:   15.59%


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        index = carType - 1
        if self.slots[index] > 0:
            self.slots[index] -= 1
            return True

        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)



#------------------------------------------------------
# Solution 2 - array w/ padding
#------------------------------------------------------

# Runtime:  96.76%
# Memory:   44.25%


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True

        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)