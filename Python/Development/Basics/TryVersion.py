class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

dog = Dog("Labrador")
print(dog.species)  # Output: Dog
print(dog.breed)    # Output: Labrador
