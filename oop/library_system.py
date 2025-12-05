class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, file_size:int):
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
    
class Library:
    def __init__(self, books=[]):
        self.books = books
    
    def add_book(self, book:Book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            book_type = book.__class__.__name__
            """if book_type == "Book":
                print(f"Book: {book.title} by {book.author}")
            elif book_type == "EBook":
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
            elif book_type == "PrintBook":
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print("Book type not found.")"""
            match book_type:
                case "Book":
                    print(f"Book: {book.title} by {book.author}")
                case "EBook":
                    print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}")
                case "PrintBook":
                    print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                case _:
                    print("Book type not found.")