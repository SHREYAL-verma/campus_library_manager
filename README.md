# campus_library_manager

A simple library system in Python, built to practise OOP ideas: abstract classes, private attributes, and class vs instance variables.

## Q&A

### 1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?

`LibraryItem` is just a general idea, so you can't create one directly. It forces every child class to write `late_fee()`. If `DVD` forgets it, Python gives a `TypeError` as soon as you try to create a DVD.

### 2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?

Two underscores make it private, so Python renames it and you get an `AttributeError`. `is_available()` lets you read the value safely without being able to change it.

### 3. What is the difference between `LibraryItem.total_items` and `self.title`?

`total_items` is one number shared by all items, like a library-wide counter. `self.title` belongs to just one item, like each book's own name.
