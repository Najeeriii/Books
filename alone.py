class Library:

    def __init__(self, list_of_books, name):
        self.booklist = list_of_books
        self.name = name
        self.lendDict = {}

        def displayBooks(self):
            print(f"We have the following books in our library:{self.name}")
            for book in self.bookslist:
                print(book)

        def lendBook(self, user, book):
            if book not in self.bookslist:
                print("Sorry, we do not have that book.")
            elif book in self.lendDict:
                print(f"The book is already being used by {self.lendDict[book]}")
            else:
                self.lendDict[book] = user
                print(
                    "Lender-Book database has been updated. You can take the book now."
                )

        def addBook(self, book):
            self.bookslist.append(book)
            print(f"{book} has been added to the book list.")

        def returnBook(self, book):
            if book in self.lendDict:
                del self.lendDict[book]
                print("Book has been reurned.")
            else:
                print("That book wasn't borrowed from us")

books = Library([
    'Rich Dad Poor Dad', '48 Laws of Power', 'Diary of Wimpy Kid'
],'Favourite Books')
user_name = input("Welcome to my library. What is your name:")

while True:
    print(
        f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:"
    )
    print(
        "1. Display Books\n2. Lend a Book\n3. Add a Book\n4 Return a Book\n5. Quit"
    )
    user_choice = input("Enter your choice to continue:")

    if user_choice not in ['1','2','3','4','5']:
        