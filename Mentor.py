from User import *
class Mentor(User):
    def __init__(self, expertise):
        super().__init__()
        self.expertise = expertise