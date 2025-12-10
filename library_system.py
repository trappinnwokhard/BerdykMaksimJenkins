class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False


class LibraryManager:
    def __init__(self):
        self.books = {} 
        self._id_counter = 1

    def add_book(self, title, author):
        new_book = Book(self._id_counter, title, author)
        self.books[self._id_counter] = new_book
        self._id_counter += 1
        return new_book

    def get_book(self, book_id):
        return self.books.get(book_id)

    def get_all_books(self):
        return list(self.books.values())

    def update_book_info(self, book_id, new_title=None, new_author=None):
        book = self.books.get(book_id)
        if not book:
            return None
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        return book

    def borrow_book(self, book_id):
        book = self.books.get(book_id)
        if book and not book.is_borrowed:
            book.is_borrowed = True
            return True
        return False  

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if book and book.is_borrowed:
            book.is_borrowed = False
            return True
        return False

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False