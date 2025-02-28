class Animal:
    """Parent class representing a generic animal."""
    def __init__(self, name, species, diet):
        self.name = name
        self.species = species
        self.diet = diet  

    def eat(self):
        """Displays what the animal eats."""
        print(f"{self.name} the {self.species} is a {self.diet.lower()} ")

    @classmethod
    def sleep(cls):
        """Class method to indicate that the species sleeps (when no instance is given)."""
        print(f"{cls.__name__} is sleeping... ")

    def __repr__(self):
        """Unambiguous string representation for debugging."""
        return f"{self.__class__.__name__}(name='{self.name}', species='{self.species}', diet='{self.diet}')"


# Child classes inheriting from Animal

class Lion(Animal):
    """Lion class (Carnivore)"""
    def __init__(self, name="Lion"):
        super().__init__(name, "Lion", "Carnivore")


class Cow(Animal):
    """Cow class (Herbivore)"""
    def __init__(self, name="Cow"):
        super().__init__(name, "Cow", "Herbivore")


class Bear(Animal):
    """Bear class (Omnivore)"""
    def __init__(self, name="Bear"):
        super().__init__(name, "Bear", "Omnivore")


# Example Usage
lion1 = Lion("Simba")
lion2 = Lion()  # No name provided, defaults to "Lion"

print(repr(lion1))  
print(repr(lion2))

lion1.eat()
Lion.sleep()

print()

cow = Cow()
bear = Bear()

print(repr(cow))   
print(repr(bear))

cow.eat()
Cow.sleep()
