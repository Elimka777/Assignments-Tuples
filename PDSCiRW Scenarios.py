def add_book(library, new_book):
    if new_book not in library:
        library.append(new_book)
        return "Book added successfully."
    else:
        return "This book is already in the library."

# Example usage
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding a new book
print(add_book(library, ("Rich Dad Poor Dad", "Robert Kiyosaki")))
# Attempting to add a duplicate book
print(add_book(library, ("1984", "George Orwell")))

# Displaying the updated library
print(library)
