import add_books
import view_all_books
from update_book import update_book
from remove_book import remove_book

all_books = []

while True:
    print("\nWelcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update a Book")
    print("4. Remove a Book")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System!")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_book(all_books)
    elif menu == "4":
        all_books = remove_book(all_books)
    else:
        print("Choose a valid number.")
