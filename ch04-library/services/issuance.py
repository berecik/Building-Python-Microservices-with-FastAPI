from typing import Optional
from repository.issuance import BookIssuanceRepository
from models.data.library import BookIssuance
from datetime import datetime
class BookIssuanceService: 
    
    def __init__(self): 
        self.repo:BookIssuanceRepository = BookIssuanceRepository()
        
    def add_book_release(self, book_release:BookIssuance): 
        return self.repo.insert_approval(book_release)
    
    def update_book_release(self, approved_id:int, book_id:Optional[int] = None, approver:Optional[str] = None): 
        result = False
        if book_id is not None: 
            result = self.repo.update_approval_details(approved_id, None, approver )
        elif approver is not None: 
            result = self.repo.update_approval_details(approved_id, approver, None )
        return result 
    
    def remove_book_release(self, approved_id:int): 
        return self.repo.delete_approval(approved_id) 
    
    def return_issued_book(self, issue_id:int, returned_date:datetime): 
        return self.repo.return_book(issue_id, returned_date )
    
    def list_book_release(self): 
        return self.repo.get_all_approvals()