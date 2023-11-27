from typing import List, Dict , Any
from faculty_mgt.repository.faculty import FacultyRepository
from faculty_mgt.models.data.faculty import Faculty

class FacultyService: 
    
    def __init__(self): 
        self.repo:FacultyRepository = FacultyRepository()
        
    def add_faculty(self, faculty:Faculty): 
        return self.repo.insert_faculty(faculty)
    
    def update_faculty(self, faculty_id:int, details:Dict[str, Any]): 
        return self.repo.update_faculty(faculty_id, details ) 
    
    def remove_faculty(self, faculty_id:int): 
        return self.repo.delete_faculty(faculty_id) 
    
    def list_faculty(self): 
        return self.repo.get_all_faculty()
    