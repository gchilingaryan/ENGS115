import datetime
import hashlib

class Student:
    def __init__(self, first_name, last_name, id, password, courses=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.password = password
        self.courses = courses

    def setFirstName(self, name):
        if name != "":
            self.first_name = name
            return self.first_name

    def setLastName(self, name):
        if name != "":
            self.last_name = name
            return self.last_name

    def setId(self, id):
        if id != "":
            self.id = id
            return self.id

    def setPassword(self, password):
        if password != "":
            self.password = password
            return self.id

    def setCourses(self, courses_list=[]):
        for i in courses_list:
            if i != "":
                self.courses.append(i)
        return self.courses

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getId(self):
        return self.id

    def getPassword(self):
        return self.password

    def getCourses(self):
        return self.courses

    def checkPassword(self, password):
        encoder = hashlib.sha224(password).hexdigest()
        if encoder == self.password:
            print("Welocme" + self.first_name)

class Course:
    def __init__(self, name, id, credit, lecturer):
        self.name = name
        self.id = id
        self.credit = credit
        self.lecturer = lecturer

    def setName(self, name):
        if name != "":
            self.name = name
            return self.name

    def setId(self, id):
        if id != "":
            self.id = id
            return self.id

    def setCredit(self, credit):
        if credit != "":
            self.credit = credit
            return self.credit

    def setLecturer(self, lecturer_name):
        if lecturer_name != "":
            self.lecturer = lecturer_name
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
    min = 0
    max = 100

    def __init__(self, name, percentage, grade, deadline, status, description):
        self.name = name
        self.percentage = percentage
        self.grade = grade
        self.deadline = deadline
        self.status = status
        self.description = description

    def setName(self, name):
        if name != "":
            self.name = name
            return self.name

    def setPercentage(self, percentage):
        if percentage != "":
            self.percentage = percentage
            return self.percentage

    def setDeadline(self, deadline):
        if deadline != "":
            self.deadline = deadline
            return self.deadline

    def setStatus(self, status):
        if status != "":
            self.status = status
            return self.status

    def getName(self):
        return self.name

    def getPercentage(self):
        return self.percentage

    def getStatus(self):
        return self.status

    def getDescription(self):
        return self.description

    def checkIfLate(self):
        return

    def checkIfGraded(self):
        return

class Grade:
    min = 0
    max = 100

    def __init__(self, grade):
        self.grade = grade

    def setGrade(self, grade):
        if grade != "":
            self.grade = grade
            return self.grade

    def getGrade(self):
        return self.grade

    def checkIfValid(self, grade):
        return