from User import *
class Admin(User):
    def __init__(self, removel_access):
        super().__init__()
        self.removel_access = removel_access