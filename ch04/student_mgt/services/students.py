from typing import Dict , Any
from student_mgt.repository.students import StudentRepository
from student_mgt.models.data.students import Student

class StudentService: 
    
    def __init__(self): 
        self.repo:StudentRepository = StudentRepository()
        
    def add_student(self, student:Student): 
        return self.repo.insert_student(student)
    
    def update_student(self, stud_id:int, details:Dict[str, Any]): 
        return self.repo.update_student(stud_id, details) 
    
    def remove_student(self, stud_id:int): 
        return self.repo.delete_student(stud_id) 
    
    def list_students(self): 
        return self.repo.get_all_students()
    
    