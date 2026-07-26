# Lab 11 — BST Deletion & Real-World Application (Library Catalogue)

## What it covers
Extends a basic BST with `delete()`, handling all three deletion cases, then
applies the completed BST to a library book catalogue keyed by ISBN.

## Concepts practiced
- **Case 1 (leaf):** node has no children, remove directly
- **Case 2 (one child):** node is replaced by its single child
- **Case 3 (two children):** copy the in-order successor's key into the
  node, then recursively delete the successor from the right subtree
- Applying a generic BST to a real-world keyed lookup problem (ISBN -> Book)
- Separating the tree structure (`bst.py`, ordered by ISBN) from the domain
  data (`library.py`, which maps ISBN -> `Book` in a dict for O(1) lookup of
  title/author, while the BST itself stays responsible for ordering/search)

## Structure
- `bst_node.py` — node definition
- `bst.py` — BST with insert, search, traversals, `find_min`, and `delete`
- `main.py` — deletion demo covering all 3 cases plus a not-found case
- `library.py` — `Book` + `LibraryCatalogue` built on top of the BST

## How to run
```
python main.py       # BST deletion demo
python library.py    # library catalogue demo
```

## Note
The book data used in `library.py`'s demo (ISBNs 10, 11, 12, 510, 1540) is
different from the sample data in the original lab handout (which used 1030,
0720, 1540, 0510, 1280). The logic is correct and fully exercises add,
find, remove, and list_all — only the demo values differ from the handout.

## Status
Complete.
