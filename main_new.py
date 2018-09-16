import datetime
import hashlib

class User:
    def __init__(self, first_name, last_name, id, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__id = id
        self.__email = email
        self.__password = password

    def setFirstName(self, name):
        if name != "":
            return self.__first_name

    def setLastName(self, name):
        if name != "":
            return self.__last_name

    def setId(self, id):
        if id != "":
            return self.__id

    def setEmail(self, email):
        if email != "":
            return self.__email

    def setPassword(self, password):
        if password != "":
            encoder = hashlib.sha224(password.encode('utf-8')).hexdigest()
            print("Welocme " + self.__first_name + " " + self.__last_name)
            self.__password = encoder
            return self.__password

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getId(self):
        return self.__id

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

class Student(User):
    def __init__(self, first_name, last_name, id, email, password):
        super().__init__(first_name, last_name, id, email, password)
        self.courses = []
        self.grades = []

    def displayInfo(self):
        print("Your ID is: " + self.getId())
        print("Your Email is: " + self.getEmail())

        courses_list = []
        for course in self.courses:
            courses_list.append(course.name)
        print("Your Courses are: " + ', '.join(courses_list))

        for i, course in enumerate(courses_list):
            print("Your assignments and grades for " + course + " are: ")
            if self.courses[i].assignments != []:
                for assignment, grade in zip(self.courses[i].assignments, self.grades):
                    print(assignment.name + " - " + str(grade.grade.getGrade()))
            else:
                print("You have no assignments for this course")

class Lecturer(User):
    def __init__(self, first_name, last_name, id, email, password):
        super().__init__(first_name, last_name, id, email, password)
        self.courses = []

    def getCourses(self):
        return self.courses

class Course:
    def __init__(self, name, id, credit, lecturer):
        self.name = name
        self.id = id
        self.credit = credit
        self.lecturer = lecturer
        self.assignments = []

    def setName(self, name):
        if name != "":
            return self.name

    def setId(self, id):
        if id != "":
            return self.id

    def setCredit(self, credit):
        if credit != "":
            return self.credit

    def setLecturer(self, lecturer_name):
        if lecturer_name != "":
            return self.lecturer

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getCredit(self):
        return self.credit

    def getLecturer(self):
        return self.lecturer

class Assignment:
    __min = 0
    __max = 100

    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description

    def setName(self, name):
        if name != "":
            return self.name

    def setDeadline(self, deadline):
        if deadline != "":
            return self.deadline

    def setDescription(self, description):
        if description != "":
            return self.description

    def getName(self):
        return self.name

    def getDeadline(self):
        return self.deadline

    def getDescription(self):
        return self.description

class AssignmentGrade:
    def __init__(self, course, assignment, percentage, grade):
        self.course = course
        self.assignment = assignment
        self.percentage = percentage
        self.grade = Grade(grade)

    def setPercentage(self, percentage):
        if percentage != "":
            return self.percentage

    def getPercentage(self):
        return self.percentage

class Grade:
    __min = 0
    __max = 100

    def __init__(self, grade):
        self.__grade = grade

    def setGrade(self, grade):
        while grade == "" or grade < Grade.__min or grade > Grade.__max:
            grade = int(input("Try again with a different number! "))
        self.__grade = grade
        return True

    def getGrade(self):
        return self.__grade

def main():
    course1 = Course("Data Structures", "ENGS115", 3, "Satenik")
    course1.setName(course1.getName())
    course1.setId(course1.getId())
    course1.setCredit(course1.getCredit())
    course1.setLecturer(course1.getLecturer())

    student1 = Student("Garik", "Chilingaryan", "A09170319", "garik_chilingaryan@edu.aua.am", "1111")
    student1.setFirstName(student1.getFirstName())
    student1.setLastName(student1.getLastName())
    student1.setId(student1.getId())
    student1.setEmail(student1.getEmail())
    student1.setPassword(student1.getPassword())

    assignment1 = Assignment("Assignment1", "2018-09-2", "MacBook Pro Parameters")
    assignment1.setName(assignment1.getName())
    assignment1.setDeadline(assignment1.getDeadline())
    assignment1.setDescription(assignment1.getDescription())

    assignment2 = Assignment("Assignment2", "2018-09-2", "Program 2 breakdown")
    assignment2.setName(assignment1.getName())
    assignment2.setDeadline(assignment1.getDeadline())
    assignment2.setDescription(assignment1.getDescription())

    assignment3 = Assignment("Assignment3", "2018-09-16", "Grade Calculator with OOP")
    assignment3.setName(assignment1.getName())
    assignment3.setDeadline(assignment1.getDeadline())
    assignment3.setDescription(assignment1.getDescription())

    course1.assignments.append(assignment1)
    course1.assignments.append(assignment2)
    course1.assignments.append(assignment3)

    student1.courses.append(course1)

    assignment1_grade = AssignmentGrade(course1, assignment1, 20, 100)
    assignment1_grade.setPercentage(assignment1_grade.getPercentage())

    assignment2_grade = AssignmentGrade(course1, assignment2, 20, 90)
    assignment2_grade.setPercentage(assignment2_grade.getPercentage())

    assignment3_grade = AssignmentGrade(course1, assignment3, 20, 80)
    assignment3_grade.setPercentage(assignment3_grade.getPercentage())

    if assignment1_grade.grade.setGrade(assignment1_grade.grade.getGrade()) == True \
            and assignment2_grade.grade.setGrade(assignment2_grade.grade.getGrade()) == True \
            and assignment3_grade.grade.setGrade(assignment3_grade.grade.getGrade()) == True:
        student1.grades.append(assignment1_grade)
        student1.grades.append(assignment2_grade)
        student1.grades.append(assignment3_grade)

    student1.displayInfo()

if __name__ == "__main__":
    main()