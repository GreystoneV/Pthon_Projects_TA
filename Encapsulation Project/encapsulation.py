# We create a class with private and protected variables
# And then we proceed to show how to ignore them and change them anyway
class Example:
    def __init__(self):
        # Here we set a protected variable
        self._dont_change_me = 0
        # This prints when an object is created
        print(f"This is what I was: {self._dont_change_me}")

    # This function sets a private variable and prints it out
    def next(self):
        self.__really_dont_change_me = 0
        print(f"I should always be: {self.__really_dont_change_me}")

    # This function changes the private variable to something we can pass in
    def why_are_you_the_way_you_are(self, why):
        self.__really_dont_change_me = why

    # This function prints out the variable with the new value
    def print_it(self):
        print(self.__really_dont_change_me)


# Create object
first = Example()
# Set protected variable to 1
first._dont_change_me = 1
# Print out changed variable
print(f"This is what I have become: {first._dont_change_me}")

# Calls the method and prints out the variable
first.next()
# Calls another method that lets us pass in a new value for the private variable
first.why_are_you_the_way_you_are("because I can")
# Calls method to print out the new value
first.print_it()


