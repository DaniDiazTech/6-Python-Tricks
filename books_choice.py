# We import only the function we need
from random import choice

def book_picker(books):
    book_choice = choice(books)
    books.remove(book_choice)    
    return f"You picked {book_choice}"

books = ["Harry potter", "Don Quixote", "Learn Python by Daniel Diaz", "Dracula"]

print(book_picker(books)) # Random choice

print(books) # Remaining books