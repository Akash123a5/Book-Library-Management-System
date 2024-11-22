from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter ISBN Number: "))
    year = int(input("Enter Publishing Year Number: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))
    
    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books Added Successully")
    
    return all_books
    