#!/usr/bin/env python3

class Dog:

    APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
    ]

    def __init__(self):
        self._name = None
        self._breed = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (type(name) == str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            self._name = name
        else:
            print("Name must be a string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")
    
    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


    
        