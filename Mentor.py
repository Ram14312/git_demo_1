from User import *
class Mentor(User):
    def __init__(self,expertise,user_id,name,email):
        super().__init__(user_id,name,email)
        self.expertise = expertise