# Create a class Book with a class variable total_books. Add a class method increment_book_count() 
# to increase the count when a new book is added.

class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count() # Update count when a new book is created

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
    @classmethod
    def display_total_books(cls):
        print(f"Total Books: {cls.total_books}")


book1 = Book("1991", "Goerge Owell") 
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book3 = Book("the Catcher in the Rye", "J.D. Salinger")

Book.display_total_books()  # Output: Total Books: 3