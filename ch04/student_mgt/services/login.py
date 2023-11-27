from student_mgt.repository.login import StudentLoginRepository
from student_mgt.models.data.students import Login

class StudentLoginService: 
    
    def __init__(self):
        self.repo:StudentLoginRepository = StudentLoginRepository()
        
    def add_student_login(self, login:Login):
        return self.repo.insert_login(login)
    
    def update_login_password(self, user_id:int, newpass:str):
        return self.repo.update_password(user_id, newpass) 
    
    def remove_student_login(self, user_id:int): 
        return self.repo.delete_login(user_id) 
    
    def get_student_login(self, username): 
        return self.repo.get_login(username)
        
    def list_login(self): 
        return self.repo.get_all_login()