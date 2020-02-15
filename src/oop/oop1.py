# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class
class Vehicle:
    pass

# derived class
class FlightVehicle(Vehicle):
    # base class: Vehicle
    pass

# derived class
class Starship(FlightVehicle):
    # base class FlightVehicle
    pass

# derived class
class GroundVehicle(Vehicle):
    # base class Vehicle
    pass

# derived class
class Airplane(FlightVehicle):
    # base class FlightVehicle
    pass

# derived class 
class Car(GroundVehicle):
    # base class GroundVehicle
    pass

class Motorcycle(GroundVehicle):
    # base class GroundVehicle
    pass