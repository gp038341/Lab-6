import pickle
class Course_grades:
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []
    def create(self):
        self.course_name = input("Enter the Course Name: ")
        for i in range(5):
            self.stu_ID.append(int(input("Enter the student ID: ")))
        for i in range(5):
            self.stu_grade.append(int(input("Enter the student grade: ")))

c1 = Course_grades()
c1.create()
c2 = Course_grades()
c2.create()
c3 = Course_grades()
c3.create()
c4 = Course_grades()
c4.create()

f = open("grades_info.dat", "wb")
pickle.dump(c1, f)
pickle.dump(c2, f)
pickle.dump(c3, f)
pickle.dump(c4, f)

f.close()

f = open("grades_info.dat", "rb")
while 1:
    try:
        data = pickle.load(f)
        print(data.course_name)
        print(data.stu_ID)
        print(data.stu_grade)
    except(EOFError):
        break
f.close()
