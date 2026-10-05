# main_menu.py - Menu that ties everything together. RUN THIS FILE LAST.
from dataset import books
from display_records import display_records
from add_record import add_record
from count_records import count_records


def main():
    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Display all books")
        print("2. Add a new book")
        print("3. Count total books")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            display_records(books)
        elif choice == "2":
            add_record(books)
        elif choice == "3":
            print(f"Total number of books: {count_records(books)}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


main()