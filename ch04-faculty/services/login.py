from repository.login import FacultyLoginRepository
from models.data.faculty import Login


class FacultyLoginService: 
    
    def __init__(self):
        self.repo:FacultyLoginRepository = FacultyLoginRepository()
        
    def add_faculty_login(self, login:Login):
        return self.repo.insert_login(login)
    
    def update_login_password(self, user_id:int, newpass:str):
        return self.repo.update_password_userid(user_id, newpass) 
    
    def remove_faculty_login(self, user_id:int): 
        return self.repo.delete_login(user_id) 
    
    def get_faculty_login(self, username:str): 
        return self.repo.get_login(username)
        
    def list_login(self): 
        return self.repo.get_all_login()