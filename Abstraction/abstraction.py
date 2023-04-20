class Car:
    def total_miles(self, miles):
        print(f"Your total miles: {miles}.")

    def trip_miles(self, miles):
        pass


class trip_check(Car):
    def trip_miles(self, miles):
        print("The miles on this trip are {}".format(miles))


obj = trip_check()
obj.total_miles("100,000")
obj.trip_miles("100")
