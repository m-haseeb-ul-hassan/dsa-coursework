# Lab 7 — Arrays and Stack Implementation

## What it covers
Four small, independent exercises in one file: a dynamic array wrapper, a
stack wrapper (both around Python lists), a linear-scan max-finder, and an
array reversal implemented using explicit stack push/pop instead of
`arr[::-1]`.

## Concepts practiced
- Wrapping built-in list operations behind a class interface (insert,
  delete, search, update)
- LIFO behavior via a manual stack (push/pop/peek)
- Guarding against invalid indices and empty-structure operations instead
  of letting them throw
- Big-O analysis: O(n) linear scan for `find_max`, O(n) for stack-based
  reversal (push pass + pop pass, constant factor dropped)

## How to run
```
python array_stack.py
```
Runs all four demos in sequence: array insert/search/update/delete, stack
push/pop/peek (including popping past empty), `find_max`, and
`reverse_array`.

## Status
Complete.
