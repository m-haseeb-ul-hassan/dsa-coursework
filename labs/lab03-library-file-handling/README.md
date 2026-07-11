# Lab 3 — Library Management System (OOP + File Handling)

Extends the Lab 1 library concept with persistent storage. Book records survive across program runs by being written to and read from a `.txt` file instead of living only in memory.

## What's inside
- `Book` class with private attributes (`__book_id`, `__title`, `__author`, `__status`) and getters.
- `Library` class that handles all file I/O: add, view, issue, return, and search books, all backed by `book.txt`.
- Menu-driven CLI loop for interacting with the system.

## Concepts practiced
- Encapsulation via private attributes
- Composition (`Library` manages `Book` objects)
- File handling: read/write/append, converting objects to file-storable strings and back

## Run it
```
python library_system.py
```

**Status:** Complete, tested.
