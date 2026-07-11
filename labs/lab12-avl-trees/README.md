# Lab 12 — AVL Trees: Rotations & Insertion

Self-balancing BST implementation in a single `avl.py` file. Covers balance factor calculation, all four rotation cases (LL, RR, LR, RL), and AVL-aware `insert()` that rebalances automatically after every insertion.

## Concepts practiced
- Balance factor = height(left) − height(right)
- Right rotation, left rotation, and the combined LR/RL double rotations
- Maintaining O(log n) height guarantees

**Status:** Completed in an earlier working session — add the finished `avl.py` here (was verified working with insertions `10, 20, 30, 25, 5, 15, 1`, confirming sorted in-order output with every balance factor in {-1, 0, 1}).
