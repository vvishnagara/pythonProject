import sqlite3

# Connect to Database
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()  # Get a cursor object


# Method to initialize book ID sequence in the database
def initialize_book_id_sequence(cursor):
    cursor.execute("INSERT OR REPLACE INTO sqlite_sequence (name, seq) VALUES ('book', 3000)")
    db.commit()


# Initialize the book ID sequence
initialize_book_id_sequence(cursor)

# Main loop for menu-driven interface
while True:
    # Display menu options and get user input
    menu = input('''Select one of the following options:
enter - Enter Book
update - Update Book
delete - Delete Book
search - Search Book
show all - Show All Books
exit - exit
: ''').lower()

    # Option to add a new book
    if menu == 'enter':
        title = input("Enter the book title:  ")
        author = input("Enter the author name: ")

        # Input validation for quantity
        while True:
            try:
                qty = int(input("Enter the quantity: "))
                if qty < 0:
                    print("Please enter a positive integer for quantity.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a positive integer for quantity.")

        # Insert book details into the database
        cursor.execute("INSERT INTO book (title, author, qty) VALUES (?,?,?)",
                       (title, author, qty))
        db.commit()
        print("Book added successfully!")

    # Option to update an existing book
    elif menu == 'update':
        print("Enter the information of the book you want to update.")
        id_book = input("What is the id of the book you are trying to update? ")

        # Check if the provided ID exists and fetch the result
        cursor.execute("SELECT * FROM book WHERE id = ?", (id_book,))
        existing_book = cursor.fetchone()

        # Check if no existing book was found with the provided ID, if so, inform the user
        if existing_book is None:
            print(f"No book found with ID {id_book}.")

        else:
            # Loop until a valid choice is made for what to update and asks user input for that choice
            while True:
                question = input("Are you trying to update the title, author, quantity, or all? ")

                if question.lower() == 'title':
                    new_title = input("Enter the new title: ")
                    cursor.execute("UPDATE book SET title = ? WHERE id = ?", (new_title, id_book))
                    print("Title updated successfully.")
                    break
                elif question.lower() == 'author':
                    new_author = input("Enter the new author: ")
                    cursor.execute("UPDATE book SET author = ? WHERE id = ?", (new_author, id_book))
                    print("Author updated successfully.")
                    break
                elif question.lower() == 'quantity':
                    new_quantity = input("Enter the new quantity: ")
                    cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (new_quantity, id_book))
                    print("Quantity updated successfully.")
                    break
                elif question.lower() == 'all':
                    new_title = input("Enter the new title: ")
                    new_author = input("Enter the new author: ")
                    new_quantity = input("Enter the new quantity: ")
                    cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?",
                                   (new_title, new_author, new_quantity, id_book))
                    print("Book updated successfully.")
                    break
                else:
                    print("Invalid choice. Please try again with 'title', 'author', 'quantity', or 'all'.")
        db.commit()

    # Option to delete a book
    elif menu == 'delete':
        title = input("Please enter the title: ")
        author = input("Please enter the author: ")
        cursor.execute("DELETE FROM book WHERE title = ? AND author = ?", (title, author))

        # Print positive message if the book exists and if not display negative message
        if cursor.rowcount > 0:
            print('You have deleted the book: ' + title)
        else:
            print('The book ' + title + ' by ' + author + ' was not found in the book database')
        db.commit()

    # Option to search for a book
    elif menu == 'search':
        title = input("Enter the title of the book you want to search for: ")
        cursor.execute("SELECT id, title, author, qty FROM book WHERE title = ?", (title,))
        results = cursor.fetchall()  # Fetch all results of the query

        # Check if any results were found, if so, print book details, otherwise inform user of no books found
        if results:
            for book in results:  # Loop through each book and print its details
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
        else:
            print("No Books Found!")  # Inform user if no books were found

    # Added extra option to display all books
    elif menu == 'show all':
        cursor.execute("SELECT * FROM BOOK")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # Option to exit the program
    elif menu == 'exit':
        print('Goodbye!!!')
        exit()

    # Handle invalid input
    else:
        print("You have made entered an invalid input. Please try again")
