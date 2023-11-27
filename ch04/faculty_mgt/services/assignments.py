from typing import List, Dict , Any
from faculty_mgt.repository.assignments import AssignmentRepository, AssignmentSubmissionRepository
from faculty_mgt.models.data.faculty import Assignment, StudentBin
from uuid import uuid4
class AssignmentService: 
    
    def __init__(self):
        self.repo:AssignmentRepository = AssignmentRepository()
    
    def add_assignment(self, assignment:Assignment): 
        return self.repo.insert_assignment(assignment)
    
    def update_assignment(self, assgn_id:int, details:Dict[str, Any]): 
        return self.repo.update_assignment(assgn_id, details) 
    
    def remove_assignment(self, assgn_id:int): 
        return self.repo.delete_assignment(assgn_id) 
    
    def list_assignment(self): 
        return self.repo.get_all_assignment()
        
class AssignmentSubmissionService: 
    
    def __init__(self): 
        self.repo:AssignmentSubmissionRepository = AssignmentSubmissionRepository()
        
    def create_workbin(self, stud_id:int, faculty_id:int): 
        bin_id = uuid4().int
        result = self.repo.create_bin(stud_id, bin_id, faculty_id )
        return (result, bin_id)
    
    def add_assigment(self, bin_id:int, assignment: Assignment ): 
        return self.repo.insert_submission(bin_id, assignment )
    
    def remove_assignment(self, bin_id:int, assignment: Assignment): 
        return self.repo.insert_submission(bin_id, assignment )
    
    def list_assignments(self, bin_id:int): 
        return self.repo.get_submissions(bin_id)


