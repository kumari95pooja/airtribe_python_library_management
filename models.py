
from abc import ABC, abstractmethod


class LibraryItem(ABC):

    total_items = 0

    def __init__(self, title, item_id):

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string.")

        if not isinstance(item_id, int) or isinstance(item_id, bool) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")

        self.title = title
        self.item_id = item_id
        self.__available = True

        LibraryItem.total_items += 1

    def is_available(self):
        return self.__available

    def mark_borrowed(self):
        self.__available = False

    def mark_returned(self):
        self.__available = True

    @abstractmethod
    def late_fee(self, days_late):
        pass

    def validate_days(self, days_late):
        if not isinstance(days_late, int) or isinstance(days_late, bool) or days_late < 0:
            raise ValueError("Days late must be a non-negative integer.")


class Book(LibraryItem):

    def __init__(self, title, item_id, author):
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Author must be a non-empty string.")

        super().__init__(title, item_id)
        self.author = author

    def late_fee(self, days_late):
        self.validate_days(days_late)
        return days_late * 2

    def describe(self):
        return f"Book: {self.title} by {self.author} (ID: {self.item_id})"


class Magazine(LibraryItem):

    def __init__(self, title, item_id, issue_number):
        if not isinstance(issue_number, int) or isinstance(issue_number, bool) or issue_number <= 0:
            raise ValueError("Issue number must be a positive integer.")

        super().__init__(title, item_id)
        self.issue_number = issue_number

    def late_fee(self, days_late):
        self.validate_days(days_late)
        return days_late * 1

    def describe(self):
        return f"Magazine: {self.title}, Issue: {self.issue_number}"


class DVD(LibraryItem):

    def __init__(self, title, item_id, duration_minutes):
        if not isinstance(duration_minutes, int) or isinstance(duration_minutes, bool) or duration_minutes <= 0:
            raise ValueError("Duration must be a positive integer.")

        super().__init__(title, item_id)
        self.duration_minutes = duration_minutes

    def late_fee(self, days_late):
        self.validate_days(days_late)
        return days_late * 5

    def describe(self):
        return f"DVD: {self.title}, Duration: {self.duration_minutes} minutes"


class Member:

    def __init__(self, name, member_id, max_items=3):

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Member name must be a non-empty string.")

        if not isinstance(member_id, int) or isinstance(member_id, bool) or member_id <= 0:
            raise ValueError("Member ID must be a positive integer.")

        if not isinstance(max_items, int) or isinstance(max_items, bool) or max_items <= 0:
            raise ValueError("Maximum items must be a positive integer.")

        self.name = name
        self.member_id = member_id
        self.max_items = max_items
        self.__borrowed = []

    def borrow(self, item):

        if not isinstance(item, LibraryItem):
            raise TypeError("Please provide a valid library item.")

        if not item.is_available():
            raise ValueError("This item is already borrowed.")

        if len(self.__borrowed) >= self.max_items:
            raise ValueError("You have reached your borrowing limit.")

        item.mark_borrowed()
        self.__borrowed.append(item)

    def return_item(self, item, days_late=0):

        if not isinstance(item, LibraryItem):
            raise TypeError("Please provide a valid library item.")

        if item not in self.__borrowed:
            raise ValueError("You have not borrowed this item.")

        # Validate before changing the borrowing status
        item.late_fee(days_late)

        item.mark_returned()
        self.__borrowed.remove(item)

        return item.late_fee(days_late)

    def borrowed_titles(self):
        return [item.title for item in self.__borrowed]
