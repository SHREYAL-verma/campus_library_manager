# models.py
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    total_items = 0  # class attribute, shared by every item

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.__available = True              # private
        LibraryItem.total_items += 1         # update the class attribute via the class name

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        # pass  # TODO: set __available to False
        self.__available = False

    def mark_returned(self):
        # pass  # TODO: set __available to True
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        pass  # every child class must implement this


class Book(LibraryItem):
    DAILY_RATE = 2

    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID {self.item_id})"

class Magazine(LibraryItem):
    DAILY_RATE = 1

    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"Magazine: {self.title} issue number {self.issue_number} (ID {self.item_id})"

class DVD(LibraryItem):
    DAILY_RATE = 5

    def __init__(self, title, item_id, duration_minutes):
        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        return days_late * self.DAILY_RATE

    def describe(self):
        return f"DVD: {self.title} of {self.duration_minutes} min (ID {self.item_id})"

# TODO: class Magazine(LibraryItem): rate 1, extra field issue_number
# TODO: class DVD(LibraryItem): rate 5, extra field duration_minutes


class Member:
    def __init__(self, name, member_id, max_items=3):
        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []                 # private list of items

    def borrow(self, item):

        if not item.is_available():
            raise ValueError(f"{item.title} is not available")
        elif len(self.__borrowed)>=self.max_items:
            raise ValueError(f"{self.name} limit is reached")
        else:
            item.mark_borrowed()
            self.__borrowed.append(item)
        # TODO: raise ValueError (with a message) if the item is not available
        # TODO: raise ValueError (with a message) if the limit is reached
        # TODO: mark the item borrowed and add it to the list
        # pass

    def return_item(self, item, days_late=0):

        if item not in self.__borrowed:
            raise ValueError(f"{item.title} is not in list")
        else:
            item.mark_returned()
            self.__borrowed.remove(item)
            # self.__borrowed = [it for it in self.__borrowed if it.title != item.title]
            return item.late_fee(days_late)

        # TODO: raise ValueError (with a message) if the item is not in the list
        # TODO: mark returned, remove from list, return item.late_fee(days_late)
        # pass

    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]
