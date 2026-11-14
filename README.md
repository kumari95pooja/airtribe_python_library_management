# Library Management System

## Project Overview

This project implements a simple campus library management system using Python OOP concepts. It supports Books, Magazines and DVDs, member borrowing and returning, late-fee calculation, exception handling and encapsulation.

## Reflection Questions

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it provides common properties and methods for all library items but should not be created directly. The `late_fee()` method is declared using `@abstractmethod`, so every child class must implement it. If DVD does not implement `late_fee()`, Python will not allow us to create a DVD object and raises a TypeError.

### 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access `item.__available` from outside the class, Python raises an AttributeError because the attribute is private and name-mangled. We use `is_available()` to check the item's availability safely without directly accessing or modifying the private attribute. This demonstrates encapsulation.

### 3. What is the difference between LibraryItem.total_items and self.title?

`LibraryItem.total_items` is a class attribute shared by all objects of the LibraryItem class and its child classes. It keeps track of the total number of library items created. In contrast, `self.title` is an instance attribute, meaning each library item object has its own title.

## How to Run

Run the following command from the project folder:

```bash
python main.py
```

## Files

- `models.py` – Contains LibraryItem, Book, Magazine, DVD and Member classes.
- `main.py` – Demonstrates borrowing, returning, late fees, exception handling and encapsulation.
- `output.txt` – Contains the console output of the final program run.