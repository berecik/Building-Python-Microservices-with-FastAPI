from typing import List, Dict , Any
from repository.signup import FacultySignupRepository
from models.data.faculty import Signup

class FacultySignupService:
    def __init__(self): 
        self.repo:FacultySignupRepository = FacultySignupRepository()
    
    def add_signup(self, signup: Signup): 
        return self.repo.add_item(signup)
    
    def get_signup(self, sign_id:int): 
        return self.repo.get_item(sign_id)
    
    def remove_signup(self, sign_id:int): 
        return self.repo.remove_item(sign_id)