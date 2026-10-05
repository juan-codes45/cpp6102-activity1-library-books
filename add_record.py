# add_record.py - TASK 2.2: Add a new record
from dataset import books
from display_records import display_records
from count_records import count_records
def add_record(records):
    """Ask for each field, build a dictionary, and append it to the list."""
    # New ID = highest existing ID + 1, so IDs never repeat
    new_id = max((b["book_id"] for b in records), default=0) + 1
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    # input() returns text, so convert the year to int and handle bad input
    while True:
        try:
            year = int(input("Enter year published: "))
            break
        except ValueError:
            print("Please enter a valid number for the year.")
    available = input("Is it available? (y/n): ").strip().lower() == "y"

    records.append({"book_id": new_id, "title": title, "author": author,
                    "year": year, "available": available})
    print(f"Book '{title}' added with ID {new_id}.")

# Quick test (runs only when this file is run directly)
if __name__ == "__main__":
    add_record(books)
    print("Total books:", count_records(books))  # should now be 6
    display_records(books)                       # new book should appear