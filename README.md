# campus_library_manager



## Q&A

### 1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?

LibraryItem is a general idea, like "a thing in the library." You never borrow a plain "item." You borrow a Book  or a DVD. Making the class abstract means Python won't let you create a LibraryItem object directly.  It forces every child class to write `late_fee()`. If `DVD` forgets it, Python gives a `TypeError` as soon as you try to create a DVD.

### 2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?

Two underscores make it private, so Python renames it and you get an `AttributeError`. `is_available()` lets you read the value safely without being able to change it.

### 3. What is the difference between `LibraryItem.total_items` and `self.title`?

`total_items` is one number shared by all items, like a library-wide counter. `self.title` belongs to just one item, like each book's own name.
