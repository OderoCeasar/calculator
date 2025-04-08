
class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving")


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sailing")


def test_vehicles():
    vehicles = [Car(), Plane(), Boat()]
    
    for vehicle in vehicles:
        vehicle.move()

# Call the test function
test_vehicles()