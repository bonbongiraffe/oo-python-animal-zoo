# - An `animal` should be instantiated with the species (e.g. "Cat", "Dog", "Rat"), a numerical, a nickname, and the Zoo instance the Animal belongs to. Keep in mind that the animal's species and nickname should not be able to change, but its weight can.
# - `Animal#nickname` should return the nickname of the animal.
# - `Animal#weight` should return the weight of the animal.
# - `Animal#species` should return the species of the animal.
# - `Animal.all` should return an list of all the animal instances.
# - `Animal#zoo` should return the zoo instance that the instance belongs to.
# - `Animal.find_by_species` should take in an animal's species as an argument and return an list of all the animals, which are of that species.

class Animal:
    all = []

    def __init__( self, species, nickname, weight, zoo ):
        self.species = species
        self.nickname = nickname
        self.weight = weight
        self.zoo = zoo
        self.all.append(self)

    def find_by_species( search_species ):
        return [x for x in Animal.all if x.species == search_species]