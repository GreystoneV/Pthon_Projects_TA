# Create new class animal. All animals here will have a sound they make and a food they eat
class Animal:
    def __init__(self, food, sound):
        self.food = food
        self.sound = sound


# Create new class dog that inherits from Animal
# We add the breed attribute to this class
class Dog(Animal):
    def __init__(self, food, sound, breed):
        super().__init__(food, sound)
        self.breed = breed


# Create new class cat that inherits from animal
# We add the personality attribute
class Cat(Animal):
    def __init__(self, food, sound, personality):
        super().__init__(food, sound)
        self.personality = personality


# Here we create an object mr_whiskers from the cat class and pass in the attributes for food, sound and
# personality
# We then print out his attributes
mr_whiskers = Cat("Meat", "Meow", "Mean")
print(f"Mr. Whiskers is {mr_whiskers.personality}. \nHe only eats {mr_whiskers.food}.\n"
      f"At the most inconvenient times you can hear him {mr_whiskers.sound}.")
