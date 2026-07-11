# Lab 9 — Singly Linked List

A from-scratch `SinglyLinkedList` implementation split across two files following modular programming practice: `node.py` defines the building-block `Node` class, `singly_linked_list.py` implements the full list.

## Methods implemented
`is_empty`, `append`, `insert(index, data)`, `pop(index=None)`, `remove_at_index(index)`, `search(data)`, `display()`

## Edge cases tested
- `pop()` on an empty list
- `insert(-1, data)` with a negative index
- `remove_at_index()` with an out-of-range index (raises `IndexError`, list stays unchanged)

## Run it
```
python singly_linked_list.py
```

**Status:** Complete, tested with driver program and edge cases.
