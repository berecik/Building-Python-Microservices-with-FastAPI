from typing import Dict , Any
from library_mgt.repository.books import BookRepository
from library_mgt.models.data.library import Book

class BookService: 
    
    def __init__(self): 
        self.repo:BookRepository = BookRepository()
        
    def add_book(self, book:Book): 
        return self.repo.insert_book(book)
    
    def update_book(self, book_id:int, details:Dict[str, Any]): 
        return self.repo.update_book(book_id, details ) 
    
    def remove_book(self, book_id:int): 
        return self.repo.delete_book(book_id) 
    
    def list_book(self): 
        return self.repo.get_all_books()
    