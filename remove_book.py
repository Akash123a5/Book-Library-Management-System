def remove_book(all_books):
    if not all_books:
        print("No books available to remove.")
        return all_books

    isbn = int(input("Enter ISBN of the book to remove: "))
    for i, book in enumerate(all_books):
        if book['isbn'] == isbn:
            print(f"Book '{book['title']}' removed successfully!")
            del all_books[i]
            return all_books
    print("Book with the given ISBN not found.")
    return all_books
