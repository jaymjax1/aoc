import math
from entries import entries

class Advent:
    def __init__(self):
        self.mass = entries

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __repr__(self):
        return 'Advent({!r})'.format(self.mass)

    def calculate_fuel_requirement(self, mass):
        if math.floor(mass/3) - 2 <= 0:
            return 0
        else:
            new_mass = math.floor(mass/3) - 2
            return new_mass + self.calculate_fuel_requirement(new_mass)

    def calculate_sum_of_fuel_requirements(self):
        sum = 0
        for x in self.mass:
            sum += self.calculate_fuel_requirement(x)
        return sum


instance = Advent()

print(instance.calculate_sum_of_fuel_requirements())
