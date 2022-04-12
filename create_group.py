class Group:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student

    def __str__(self):
        str = ""
        for student in self.students:
          str += student.__str__()
        return str
