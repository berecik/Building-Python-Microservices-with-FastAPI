from typing import List, Dict , Any
from faculty_mgt.repository.signup import FacultySignupRepository
from faculty_mgt.models.data.faculty import Signup

class FacultySignupService:
    def __init__(self): 
        self.repo:FacultySignupRepository = FacultySignupRepository()
    
    def add_signup(self, signup: Signup): 
        return self.repo.insert_item(signup)
    
    def get_signup(self, sign_id:int): 
        return self.repo.get_item(sign_id)
    
    def remove_signup(self, sign_id:int): 
        return self.repo.delete_item(sign_id)