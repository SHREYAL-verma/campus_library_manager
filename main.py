# main.py
from models import Book, Member, Magazine, DVD  # TODO: also import Magazine, DVD

book = Book("Python 101", 1, "A. Rao")
# TODO: create one Magazine and one DVD
magazine = Magazine("Tech Today", 2, 45)
dvd = DVD("Space Movie", 3, 120)

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 1. Borrowing with error handling
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. TODO: trigger the borrow-limit error and the not-borrowed error, catching each
# Bob can only borrow 1 item, so the second borrow should fail
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

# Bob never borrowed the book, so returning it should fail
try:
    bob.return_item(book)  # should fail: Bob does not have this book
except ValueError as e:
    print("Could not return:", e)

# 3. Polymorphism: one loop, no type checks
items = [book, magazine, dvd]  # TODO: add the magazine and the DVD
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Class attribute shared by all objects
print("Total items created:", Book.total_items)
