# Lab 6 — Time and Space Complexity Analysis

Theory-only lab (no code deliverable). Analyzed 8 given Python programs and
determined their time/space complexity using Big-O notation, with reasoning
shown for each.

## Concepts practiced
- Counting loop iterations and per-iteration cost
- Recursion depth vs. total call count (factorial, fibonacci, Tower of Hanoi)
- Amortized/aggregate cost across multiple function calls (array reversal
  via 3 reverse() calls)
- Space cost of recursion stacks vs. iterative solutions
- Cost of Python list slicing (`list[1:]` is O(k), not O(1))

## Summary of answers

| # | Program | Time | Space | Key reasoning |
|---|---------|------|-------|----------------|
| 1 | findLargest + printArray | O(n) | O(1) | Two sequential O(n) passes, no extra structures |
| 2 | leftRotate (reversal algorithm) | O(n) | O(1) | 3 calls to reverse(), total work sums to O(n) |
| 3 | factorial (recursive) | O(n) | O(n) | n+1 calls, one stack frame per call |
| 4 | binary_search (iterative) | O(log n) | O(1) | Search space halves each iteration, only 3 variables used |
| 5 | fibonacci (naive recursive) | O(2ⁿ) | O(n) | ~2ⁿ total calls, but max stack depth is only n |
| 6 | list_sum_recursive | O(n²) | O(n²) | Each call slices the list — slicing costs add up to n(n+1)/2 |
| 7 | count_divisions | O(log n) | O(1) | n halves each loop, only fixed variables used |
| 8 | Tower of Hanoi | O(2ⁿ) | O(n) | 2ⁿ - 1 total moves, but max recursion depth is n |

Full worked reasoning for each question is in the original submission.

## Status
Complete (theory only, no code deliverable).
