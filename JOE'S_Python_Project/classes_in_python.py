class student:
    student_id = 0
    student_name = ""
    student_age = 0
    def __init__(self, student_id, student_name, student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age

    def displaystudent(self):
        print("The student details are:", "name:" ,self.student_name, "Age:", self.student_age)

student1 = student("100", "Caleb", "20")
student1.displaystudent()

#Inheritance lesson
class person:
    person_name = ""
    person_residence = ""
    person_age = 0

    def __init__(them,name,residence,age):
        them.person_name = name
        them.person_residence = residence
        them.person_age = age

    def printTheDetails(them):
        print("The person details are:",them.person_name,"and Residence:",them.person_residence)



class Student(person):
    uniform = ""

    def __init__(them,name,residence,age,uni):
        super().__init__(name,residence,age)
        them.uniform = uni
        print("The student uniform is:",them.uniform)

student1 = Student("Joe","Brazil",20,"Black")
student1.printTheDetails()
