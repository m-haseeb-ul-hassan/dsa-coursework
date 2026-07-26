# Lab 2 — Abstraction & Encapsulation (Hospital Appointment System)

## What it covers
A hospital appointment system built to practice Python's `abc` module and
access-control conventions. `Appointment` is an abstract base class with two
abstract methods (`calculate_fee`, `get_appointment_details`) implemented
differently by `GeneralAppointment` (flat 1500 PKR fee) and
`SpecialistAppointment` (fee scales with years of experience). Appointment
status is stored as a private attribute (`__status`) and can only change
through `set_status()`, which blocks invalid values and blocks any change
once a status is `"Completed"`.

## Concepts practiced
- Abstract base classes (`ABC`, `@abstractmethod`)
- Protected (`_attr`) vs private (`__attr`) attributes and Python's name mangling
- Getter/setter access control
- Polymorphism across two concrete subclasses of the same abstract class

## How to run
```
python hospital_appointment.py
```
Runs a simulation: creates 2 general + 2 specialist appointments, prints all
of them, then tries a mix of valid and invalid status updates (including one
against an appointment already marked `Completed`) to demonstrate the guard
rails.

## Status
Complete.
