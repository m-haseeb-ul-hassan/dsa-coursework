# Lab 1 — OOP Revision: Library & Hospital Management

Two small systems in one file, built to revise core OOP from Programming II before diving into DSA.

## What's inside
- **Library System** — `LibraryItem` base class with a `Book` subclass (inheritance), borrow/return logic with availability tracking.
- **Hospital System** — `Person` base class extended into `Patient` and `Doctor`, plus `Appointment` (composition) and `Hospital` (aggregation) classes tying everything together.

## Concepts practiced
- Inheritance (`Book` → `LibraryItem`, `Patient`/`Doctor` → `Person`)
- Composition (`Appointment` holds `Patient` and `Doctor` objects)
- Aggregation (`Hospital` manages lists of patients, doctors, appointments)

## Run it
```
python lab1.py
```

**Status:** Complete, tested.
