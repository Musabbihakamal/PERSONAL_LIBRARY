import json
import os

data_file = "library.txt"  # FIXED: added .txt extension properly

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("ENTER THE TITLE OF THE BOOK: ")
    author = input("ENTER THE NAME OF THE AUTHOR: ")
    year = input("ENTER THE YEAR OF THE BOOK: ")
    genre = input("ENTER THE GENRE OF THE BOOK: ")
    read = input("HAVE YOU READ THE BOOK? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("ENTER THE TITLE OF THE BOOK TO REMOVE FROM YOUR LIBRARY: ").lower()
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title]  # Update the list in place
    if len(library) < initial_length:
        save_library(library)
        print(f"Book '{title}' removed successfully!")
    else:
        print("No matching book found to remove.")

def search_library(library):
    search_by = input("SEARCH BY (title/author): ").lower()
    if search_by not in ["title", "author"]:
        print("Invalid search field.")
        return

    search_term = input(f"ENTER THE {search_by}: ").lower()
    result = [book for book in library if search_term in book[search_by].lower()]

    if result:
        for book in result:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No book found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

def library_count(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"TOTAL BOOKS: {total_books}")
    print(f"PERCENTAGE READ: {percentage_read:.2f}%")

def main():
    library = load_library()
    while True:
        print("\n📚 WELCOME TO LIBRARY MANAGER")
        print("MENU")
        print("1. ADD A BOOK")
        print("2. REMOVE A BOOK")
        print("3. SEARCH THE LIBRARY")
        print("4. DISPLAY ALL BOOKS")
        print("5. DISPLAY STATISTICS")
        print("6. EXIT")

        choice = input("ENTER YOUR CHOICE (1-6): ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_library(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            library_count(library)
        elif choice == '6':
            print("📁 Library saved. Goodbye! 👋")
            save_library(library)
            break
        else:
            print("❌ INVALID CHOICE. PLEASE TRY AGAIN.")

if __name__ == "__main__":
    main()

