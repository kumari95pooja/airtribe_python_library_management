
from models import Book, Magazine, DVD, Member, LibraryItem


# --------------------------------------------------
# 1. Creating Library Items - Valid Arguments
# --------------------------------------------------

print("\n--- Creating Library Items ---")

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Python Today", 2, 45)
dvd = DVD("Python Tutorial", 3, 120)

print(book.describe())
print(magazine.describe())
print(dvd.describe())


# --------------------------------------------------
# 2. Testing Invalid Arguments During Object Creation
# --------------------------------------------------

print("\n--- Invalid Object Arguments ---")

invalid_objects = [
    lambda: Book("", 4, "A. Rao"),
    lambda: Book("Python", -1, "A. Rao"),
    lambda: Book("Python", 4, ""),
    lambda: Magazine("Tech", 5, -10),
    lambda: DVD("Tutorial", 6, 0),
    lambda: Member("", 103),
    lambda: Member("John", -2),
    lambda: Member("John", 104, 0)
]

for create_object in invalid_objects:
    try:
        create_object()
    except (ValueError, TypeError) as e:
        print("Invalid argument:", e)


# --------------------------------------------------
# 3. Creating Members - Valid Arguments
# --------------------------------------------------

print("\n--- Creating Members ---")

alice = Member("Alice", 101)
bob = Member("Bob", 102, 1)

print("Members created successfully.")


# --------------------------------------------------
# 4. Borrowing Items
# --------------------------------------------------

print("\n--- Borrowing Items ---")

try:
    alice.borrow(book)
    print("Alice borrowed the book successfully.")
except (ValueError, TypeError) as e:
    print("Error:", e)


# Trying to borrow an already borrowed item
try:
    bob.borrow(book)
except (ValueError, TypeError) as e:
    print("Error:", e)


# Trying to borrow an invalid object
try:
    alice.borrow("Python 101")
except (ValueError, TypeError) as e:
    print("Error:", e)


# --------------------------------------------------
# 5. Checking Borrowing Limit
# --------------------------------------------------

print("\n--- Borrowing Limit ---")

try:
    bob.borrow(magazine)
    print("Bob borrowed the magazine successfully.")
except (ValueError, TypeError) as e:
    print("Error:", e)

# Bob's maximum limit is 1
try:
    bob.borrow(dvd)
except (ValueError, TypeError) as e:
    print("Error:", e)


# --------------------------------------------------
# 6. Trying to Return an Item Not Borrowed
# --------------------------------------------------

print("\n--- Return Item Validation ---")

try:
    bob.return_item(book)
except (ValueError, TypeError) as e:
    print("Error:", e)

# Trying to return an invalid object
try:
    alice.return_item("Python 101")
except (ValueError, TypeError) as e:
    print("Error:", e)


# --------------------------------------------------
# 7. Calculating Late Fees Using Polymorphism
# --------------------------------------------------

print("\n--- Late Fees ---")

items = [book, magazine, dvd]

for item in items:
    print(item.describe())

    try:
        print("Late fee for 3 days: Rs", item.late_fee(3))
    except (ValueError, TypeError) as e:
        print("Error:", e)


# --------------------------------------------------
# 8. Testing Invalid Late Fee Arguments
# --------------------------------------------------

print("\n--- Invalid Late Fee Arguments ---")

invalid_days = [-2, 2.5, "three"]

for days in invalid_days:
    try:
        print("Late fee:", book.late_fee(days))
    except (ValueError, TypeError) as e:
        print("Error:", e)


# --------------------------------------------------
# 9. Returning Borrowed Items
# --------------------------------------------------

print("\n--- Returning Items ---")

try:
    fee = alice.return_item(book, 3)
    print("Alice returned the book. Fee: Rs", fee)
except (ValueError, TypeError) as e:
    print("Error:", e)

try:
    fee = bob.return_item(magazine, 3)
    print("Bob returned the magazine. Fee: Rs", fee)
except (ValueError, TypeError) as e:
    print("Error:", e)


# --------------------------------------------------
# 10. Checking Item Availability and Encapsulation
# --------------------------------------------------

print("\n--- Item Availability ---")

try:
    print(book.__available)
except AttributeError:
    print("Cannot access private availability directly.")

print("Book available:", book.is_available())
print("Magazine available:", magazine.is_available())
print("DVD available:", dvd.is_available())


# --------------------------------------------------
# 11. Checking Borrowed Items
# --------------------------------------------------

print("\n--- Borrowed Items ---")

print("Alice borrowed items:", alice.borrowed_titles())
print("Bob borrowed items:", bob.borrowed_titles())


# --------------------------------------------------
# 12. Total Library Items
# --------------------------------------------------

print("\n--- Total Library Items ---")

print("Total library items:", LibraryItem.total_items)