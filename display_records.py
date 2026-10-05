# display_records.py - TASK 2.1: Display all records
from dataset import books

def display_records(records):
    """Loop through the list and print every book's fields."""
    if len(records) == 0:
        print("No records to display.")
        return
    print("\n--- LIBRARY BOOK RECORDS ---")
    for book in records:  # each 'book' is one dictionary
        status = "Available" if book["available"] else "Borrowed"
        print(f"ID: {book['book_id']} | {book['title']} | {book['author']} | {book['year']} | {status}")


# Quick test (runs only when this file is run directly)
if __name__ == "__main__":
    display_records(books)