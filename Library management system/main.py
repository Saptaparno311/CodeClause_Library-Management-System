class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed from the library.")
        else:
            print(f"Book '{book}' not found in the library.")

    def show_books(self):
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

    def show_number_of_books(self):
        print(f"Number of books in the library: {len(self.books)}")

    def check_library(self):
        if self.books:
            print("Library is not empty.")
        else:
            print("Library is empty.")


# Create a Library object
library = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Show Books")
    print("4. Show Number of Books")
    print("5. Check Library")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        book_name = input("Enter the book name: ")
        library.add_book(book_name)
    elif choice == '2':
        book_name = input("Enter the book name: ")
        library.remove_book(book_name)
    elif choice == '3':
        library.show_books()
    elif choice == '4':
        library.show_number_of_books()
    elif choice == '5':
        library.check_library()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
