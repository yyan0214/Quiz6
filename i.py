class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

class LibraryCatalog:
    def add_book(self, book):
        raise NotImplementedError("add_book method not implemented")

    def remove_book(self, book):
        raise NotImplementedError("remove_book method not implemented")

    def search_by_title(self, title):
        raise NotImplementedError("search_by_title method not implemented")

    def search_by_author(self, author):
        raise NotImplementedError("search_by_author method not implemented")

    def search_by_genre(self, genre):
        raise NotImplementedError("search_by_genre method not implemented")

class BookManager:
    def borrow_book(self, book, user):
        raise NotImplementedError("borrow_book method not implemented")

    def return_book(self, book, user):
        raise NotImplementedError("return_book method not implemented")

class ReportGenerator:
    def generate_borrowings_report(self):
        raise NotImplementedError("generate_borrowings_report method not implemented")

    def generate_overdue_books_report(self):
        raise NotImplementedError("generate_overdue_books_report method not implemented")

    def generate_popularity_report(self):
        raise NotImplementedError("generate_popularity_report method not implemented")

class GuestUser(LibraryCatalog):
    def search_by_title(self, title):
        print(f"Guest user searching for book with title: {title}")

    def search_by_author(self, author):
        print(f"Guest user searching for book by author: {author}")

    def search_by_genre(self, genre):
        print(f"Guest user searching for book in genre: {genre}")

class Librarian(LibraryCatalog, BookManager, ReportGenerator):
    def add_book(self, book):
        print(f"Librarian adding book: {book.title}")

    def remove_book(self, book):
        print(f"Librarian removing book: {book.title}")

    def borrow_book(self, book, user):
        print(f"Librarian borrowing book: {book.title} for user: {user}")

    def return_book(self, book, user):
        print(f"Librarian returning book: {book.title} for user: {user}")

    def generate_borrowings_report(self):
        print("Generating borrowings report")

    def generate_overdue_books_report(self):
        print("Generating overdue books report")

    def generate_popularity_report(self):
        print("Generating popularity report")

def main():
    # Dummy data
    book = Book("Harry Potter", "J.K. Rowling", "Fantasy")
    user = "John Doe"

    # Guest user functionality
    guest_user = GuestUser()
    guest_user.search_by_title("Harry Potter")
    guest_user.search_by_genre("Fantasy")

    # Librarian functionality
    librarian = Librarian()
    librarian.add_book(book)
    librarian.remove_book(book)
    librarian.borrow_book(book, user)
    librarian.return_book(book, user)
    librarian.generate_borrowings_report()
    librarian.generate_overdue_books_report()
    librarian.generate_popularity_report()

if __name__ == "__main__":
    main()
