# count_records.py - TASK 2.3: Count the total number of records
from dataset import books


def count_records(records):
    """len() returns the number of items (books) in the list."""
    return len(records)


# Quick test (runs only when this file is run directly)
if __name__ == "__main__":
    print("Total books:", count_records(books))