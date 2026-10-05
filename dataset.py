# dataset.py - TASK 1: Design the dataset
# Each book is a dictionary; all books are stored in a list.
books = [
    {"book_id": 1, "title": "Weep Not, Child", "author": "Ngugi wa Thiong'o", "year": 1964, "available": True},
    {"book_id": 2, "title": "Born a Crime", "author": "Trevor Noah", "year": 2016, "available": False},
    {"book_id": 3, "title": "Things Fall Apart", "author": "Chinua Achebe", "year": 1958, "available": True},
    {"book_id": 4, "title": "Python Crash Course", "author": "Eric Matthes", "year": 2019, "available": True},
    {"book_id": 5, "title": "Half of a Yellow Sun", "author": "Chimamanda Ngozi Adichie", "year": 2006, "available": False},
]

# This block only runs when you run dataset.py directly (a quick test)
if __name__ == "__main__":
    print(books[0])