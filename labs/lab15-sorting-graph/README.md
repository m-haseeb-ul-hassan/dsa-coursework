# Lab 15 — Sorting Algorithms and Graph (Adjacency Matrix + BFS)

## Sorting
- **Bubble Sort** — optimized with early exit when no swaps occur; used to find the top 3 highest marks from a list of student scores.
- **Insertion Sort** — sorts a list of names alphabetically, printing the list after each insertion step.

## Graph
- `GraphMatrix` class representing an undirected graph as an adjacency matrix, with `add_edge`, `remove_edge`, `add_vertex`, `remove_vertex`, and `display`.
- **BFS traversal** using a queue and a visited array, traversing neighbors via the adjacency matrix row of the current node.

## Run it
```
python sorting_graph.py
```
(Prompts for student count/marks and name count/names before running the graph demo.)

**Status:** Complete, tested.
