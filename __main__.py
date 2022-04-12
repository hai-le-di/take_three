from create_group import*
from create_human import*
from create_student import*

student_one = Student("Hunter", 24, "male", "business")
student_two = Student("Ricky", 30, "male", "music production")
group_a = Group()
group_a.add_student(student_one)
group_a.add_student(student_two)

print(group_a)
find_a = group_a.find_student("Ricky")
print(find_a)
