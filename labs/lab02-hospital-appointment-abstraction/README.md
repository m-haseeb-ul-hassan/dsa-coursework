# Lab 2 — Hospital Appointment System (Abstraction & Encapsulation)

Builds on Lab 1's hospital theme, this time focused on abstract base classes and access control rather than plain inheritance.

## Requirements (per lab handout)
- Abstract class `Appointment` (via Python's `abc` module) with protected attributes and abstract methods `calculate_fee()` and `get_appointment_details()`.
- Two concrete subclasses: `GeneralAppointment` (fixed fee) and `SpecialistAppointment` (fee scales with experience).
- Private `__status` attribute on appointments, with validated getter/setter (`Booked` / `Completed` / `Cancelled`, no changes after `Completed`).
- `Hospital` class to manage and update appointments.

**Status:** Pending — only the lab handout was available, no completed implementation found yet. Add the solved `.py` file here once located or rewritten.
