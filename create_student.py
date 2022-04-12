from create_human import*
class Student(Human):

    def __init__(self, name, age, gender, major):
        super().__init__(name, age, gender)
        self.major = major
    def __str__(self):
        human_str = super().__str__()
        return str(human_str) + ", major = {} \n".format(self.major)
