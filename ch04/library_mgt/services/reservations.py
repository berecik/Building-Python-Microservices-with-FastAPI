from library_mgt.repository.reservations import BookRequestRepository
from library_mgt.models.data.library import BookRequest

class BookRequestService: 
    
    def __init__(self): 
        self.repo:BookRequestRepository = BookRequestRepository()
        
    def add_book_request(self, book_request:BookRequest): 
        return self.repo.insert_request(book_request)
    
    def update_book_request(self, req_id:int, book_id:int): 
        return self.repo.update_requested_book(req_id, book_id) 
    
    def remove_book_request(self, req_id:int): 
        return self.repo.delete_request(req_id) 
    
    def list_book_request(self): 
        return self.repo.get_all_requests()
    