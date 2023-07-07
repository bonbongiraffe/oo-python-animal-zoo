from zoo import Zoo
from animal import Animal
import ipdb
# - A `zoo` should be initialized with a name and a location, which should both be passed as strings.
# - `Zoo#location` should return the location of the zoo instance.
# - `Zoo#name` should return the name of the zoo instance.
# - `Zoo.all` should return an list of all the zoo instances.
# - `Zoo#animals` should return all the animals that a specific instance of a zoo has.
# - `Zoo#animal_species` should return an list of all the species (as strings) of the animals in the zoo. However, if you have two dogs, it should only return one "Dog" string (aka an **unique** list).
# - `Zoo#find_by_species` should take in an animal's species as an argument and return an list of all the animals in that zoo, which are of that species.
# - `Zoo#animal_nicknames` should return an list of all the nicknames of animals that a specific instance of a zoo has.
# - `Zoo.find_by_location` should take in a location as an argument and return an list of all the zoos within that location.

# - An `animal` should be instantiated with the species (e.g. "Cat", "Dog", "Rat"), a numerical, a nickname, and the Zoo instance the Animal belongs to. Keep in mind that the animal's species and nickname should not be able to change, but its weight can.
# - `Animal#nickname` should return the nickname of the animal.
# - `Animal#weight` should return the weight of the animal.
# - `Animal#species` should return the species of the animal.
# - `Animal.all` should return an list of all the animal instances.
# - `Animal#zoo` should return the zoo instance that the instance belongs to.
# - `Animal.find_by_species` should take in an animal's species as an argument and return an list of all the animals, which are of that species.
zoo1 = Zoo("Jamanji", "Africa")
zoo2 = Zoo("Paris", "France")
animal1 = Animal("Cat", "Garfield", 80, zoo1)
animal2 = Animal("Dog", "Shaggy", 40, zoo1)
animal3 = Animal("Rat", "Remy", 2, zoo2)
ipdb.set_trace()
