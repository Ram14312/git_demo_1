from User import *
class Student(User):

    def __init__(self,enrolled_courses):
        super().__init__()
        self.enrolled_courses = enrolled_courses