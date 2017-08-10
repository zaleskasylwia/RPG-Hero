class Character:
    def __init__(self, first_name, last_name, race):
        if type(first_name) is str nad type(last_name) is str and type(race) is str:
            self.first_name = first_name
            self.last_name = last_name
            self.race = race
        else:
            raise TypeError

    def __str__(self):
        return "Name: {} {} is from race {}".format(self.first_name, self.last_name, self.race)

