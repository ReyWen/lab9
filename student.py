from abc import abstractmethod


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class UniversityMember(Human):
    def __init__(self, name, surname, age, university, faculty):
        super().__init__(name, surname, age)
        self.university = university
        self.faculty = faculty

    @abstractmethod
    def help(self, other):
        pass


class Professor(UniversityMember):
    def __init__(self, name, surname, age, university, faculty):
        super().__init__(name, surname, age, university, faculty)

    def help(self, student):
        if self.faculty == student.faculty:
            student.grade += 5


class Student(UniversityMember):
    def __init__(self, name, surname, age, university, faculty, year, grade):
        super().__init__(name, surname, age, university, faculty)
        self.year = year
        self.grade = grade

    def request_help(self, other):
        if isinstance(other, UniversityMember):
            other.help(self)

    def help(self, student):
        if self.faculty == student.faculty and self.year >= student.year:
            student.grade += 1
