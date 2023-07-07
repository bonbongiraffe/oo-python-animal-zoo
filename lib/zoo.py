from animal import Animal
# - A `zoo` should be initialized with a name and a location, which should both be passed as strings.
# - `Zoo#location` should return the location of the zoo instance.
# - `Zoo#name` should return the name of the zoo instance.
# - `Zoo.all` should return an list of all the zoo instances.
# - `Zoo#animals` should return all the animals that a specific instance of a zoo has.
# - `Zoo#animal_species` should return an list of all the species (as strings) of the animals in the zoo. However, if you have two dogs, it should only return one "Dog" string (aka an **unique** list).
# - `Zoo#find_by_species` should take in an animal's species as an argument and return an list of all the animals in that zoo, which are of that species.
# - `Zoo#animal_nicknames` should return an list of all the nicknames of animals that a specific instance of a zoo has.
# - `Zoo.find_by_location` should take in a location as an argument and return an list of all the zoos within that location.

class Zoo:
    all = []

    def __init__( self, name, location ):
        self.name = name
        self.location = location
        self.all.append(self)

    def animals( self ):
        animal_list = [ animal for animal in Animal.all if animal.zoo == self ]
        return animal_list

    def animal_species( self ):
        species_list = [] 
        for animal in self.animals():
            if animal.species not in species_list:
                species_list.append(animal.species)
        return species_list
    
    def find_by_species( self, search_species ):
        search_animal_list = [ animal for animal in self.animals() if animal.species == search_species ]
        return search_animal_list
    
    def animal_nicknames( self ):
        nickname_list = [ animal.nickname for animal in self.animals() ]
        return nickname_list
    
    @classmethod
    def find_by_location( self, search_location ):
        zoo_list = [ zoo for zoo in self.all if zoo.location == search_location ]
        return zoo_list

    #property methods follow:
    def get_name( self ):
        return self._name
    
    def set_name( self, name ):
        if type(name) == str:
            self._name = name
        else:
            raise Exception("Zoo name must be a string.")

    def get_location( self ):
        return self._location 
    
    def set_location( self, location ):
        if type(location) == str:
            self._location = location
        else:
            raise Exception("Location must be a string.")
    
    location = property( get_location, set_location )
    name = property( get_name, set_name )