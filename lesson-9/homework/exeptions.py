import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"

class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException("Borrowing limit exceeded! Return a book first.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print("This book was not borrowed by the member.")
    
    def __str__(self):
        books = ', '.join(book.title for book in self.borrowed_books) or 'No books borrowed'
        return f"Member: {self.name}, Borrowed Books: {books}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added to the library.")

    def add_member(self, name):
        self.members.append(Member(name))
        print(f"Member '{name}' added to the library.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException("Book not found in the library.")

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        print("Member not found.")
        return None
    
    def borrow_book(self, member_name, book_title):
        try:
            member = self.find_member(member_name)
            if member is None:
                return
            book = self.find_book(book_title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if member is None:
            return
        try:
            book = self.find_book(book_title)
            member.return_book(book)
        except BookNotFoundException:
            print("Cannot return a book that does not exist.")
    
    def display_books(self):
        for book in self.books:
            print(book)
        if not self.books:
            print("No books available in the library.")
    
    def display_members(self):
        for member in self.members:
            print(member)
        if not self.members:
            print("No members found.")
    
    def menu(self):
        while True:
            print("\nLibrary Management System")
            print("1. Add Book")
            print("2. Add Member")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. View Books")
            print("6. View Members")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                self.add_book(title, author)
            elif choice == "2":
                name = input("Enter member name: ")
                self.add_member(name)
            elif choice == "3":
                member_name = input("Enter member name: ")
                book_title = input("Enter book title: ")
                self.borrow_book(member_name, book_title)
            elif choice == "4":
                member_name = input("Enter member name: ")
                book_title = input("Enter book title: ")
                self.return_book(member_name, book_title)
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                self.display_members()
            elif choice == "7":
                print("Exiting the library system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library = Library()
    library.menu()
