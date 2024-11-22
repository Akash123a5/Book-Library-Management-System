def update_book(all_books):
    if not all_books:
        print("No books available to update.")
        return all_books

    isbn = int(input("Enter ISBN of the book to update: "))
    for book in all_books:
        if book['isbn'] == isbn:
            print("Book found!")
            print("Enter new details (leave blank to keep current value):")
            book['title'] = input(f"Title ({book['title']}): ") or book['title']
            book['author'] = input(f"Author ({book['author']}): ") or book['author']
            try:
                book['year'] = int(input(f"Year ({book['year']}): ") or book['year'])
                book['price'] = int(input(f"Price ({book['price']}): ") or book['price'])
                book['quantity'] = int(input(f"Quantity ({book['quantity']}): ") or book['quantity'])
            except ValueError:
                print("Invalid input. Keeping previous values for numeric fields.")
            print("Book updated successfully!")
            return all_books
    print("Book with the given ISBN not found.")
    return all_books
