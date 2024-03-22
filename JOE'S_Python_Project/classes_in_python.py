class student:
    student_id = 0
    student_name = ""
    student_age = 0
    def __init__(self, student_id, student_name, student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age

    def displaystudent(self):
        print("The student details are:", self.student_name, "Age:", self.student_age)

student1 = student("100", "Caleb", "20")
student1.displaystudent()
