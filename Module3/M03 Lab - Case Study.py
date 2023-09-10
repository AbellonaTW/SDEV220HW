class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def __str__(self):
        return "Vehicle type: " + self.vehicle_type + "Year of vehicle: " + self.year + "Vehicle make: " + self.make + "Model of vehicle: " + self.model + "Number of doors of the vehicle: " + self.doors + "Type of roof on vehicle: " + self.roof
    
if __name__ == "__main__":
    vehicle_type = input("Please enter vehicle type: ")
    year = input("Please enter year of the vehicle: ")
    make = input("Please enter the make of vehicle: ")
    model = input("Please enter the model of the vehicle: ")
    doors = input("Please enter the quantity of doors of the vehicle: ")
    roof = input("Please state the type of roof on the vehicle if it exists: ")

    Vehicle_request_output = Automobile(vehicle_type, year, make, model, doors, roof)
    print("The details inputed of the vehicle are as follows: ")
    print(Vehicle_request_output)