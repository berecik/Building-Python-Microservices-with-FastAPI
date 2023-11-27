from student_mgt.repository.signup import StudentSignupRepository
from student_mgt.models.data.students import Signup  

class StudentSignupService: 
    
    def __init__(self): 
        self.repo:StudentSignupRepository = StudentSignupRepository()
    
    def add_signup(self, signup: Signup): 
        return self.repo.insert_item(signup)
    
    def get_signup(self, sign_id:int): 
        return self.repo.get_item(sign_id)
    
    def remove_signup(self, sign_id:int): 
        return self.repo.delete_item(sign_id)