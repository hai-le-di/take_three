class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return "name = {}, age = {}, gender = {}".format(self.name, self.age, self.gender)
