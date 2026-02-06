# -------------------- BOOK CLASS --------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id} | {self.title} by {self.author} | Status: {status}"


# -------------------- LIBRARY CLASS --------------------
class Library:
    def __init__(self):
        self.books = []

    # Add book
    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("✅ Book added successfully!")

    # Display books
    def display_books(self):
        if not self.books:
            print("❌ No books in library.")
            return
        print("\n📚 Library Books:")
        for book in self.books:
            print(book)

    # Issue book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print("✅ Book issued successfully!")
                else:
                    print("❌ Book already issued.")
                return
        print("❌ Book not found.")

    # Return book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print("✅ Book returned successfully!")
                else:
                    print("❌ Book was not issued.")
                return
        print("❌ Book not found.")


# -------------------- MAIN MENU (CLI) --------------------
def main():
    library = Library()

    while True:
        print("\n------ Library Management System ------")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()
