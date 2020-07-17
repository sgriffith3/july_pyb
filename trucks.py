
class Truck:
    def __init__(self, color, bed, seats = 5, tires = 22, drivetrain = 'front'):
        self.color = color
        self.seats = seats
        self.bed = bed
        self.tires = tires
        self.drivetrain = drivetrain
        self.pos = 0

    # truck attributes
    # color
    # number of seats
    # bed size
    # tire size
    # Drivetrain
        
    # truck methods
    
    # drive forward
    
    def drive(self, num_spaces=1):
        self.pos += num_spaces
        # self.pos = self.pos + 1
        print(f"Current position is {self.pos}")


    # drive in reverse
    def reverse(self, num_spaces=1):
        self.pos -= num_spaces
        print(f"Current position is {self.pos}")


betsy = Truck('blue', 5)

print(betsy)
print(type(betsy))


print(betsy.color)
print(betsy.seats)
print(betsy.bed)
print(betsy.tires)
print(betsy.drivetrain)

print("Driving the truck")
betsy.drive(3)
betsy.drive(7)
print("Backing up")
betsy.reverse(4)
betsy.reverse(9)


