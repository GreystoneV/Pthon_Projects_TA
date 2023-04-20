# Create car class
class Car:
    # Create method to tell the total miles
    def total_miles(self, miles):
        print(f"Your total miles: {miles}.")
    # Create methos to tell trip miles but don't pass anything in
    def trip_miles(self, miles):
        pass


# Create class to check for trip miles that inherits from class car
class trip_check(Car):
    # Make use of the inherited method but use what was passed in
    def trip_miles(self, miles):
        print("The miles on this trip are {}".format(miles))


# Create object
obj = trip_check()
# Use method from parent class
obj.total_miles("100,000")
# Use tip_miles method in child class
obj.trip_miles("100")
