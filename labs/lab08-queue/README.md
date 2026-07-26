# Lab 8 — Queue Implementation

## What it covers
Two ways to build a FIFO queue: a straightforward list-based `Queue`
(`append` for enqueue, `pop(0)` for dequeue), and `QueueUsingStacks`, which
simulates a queue using two LIFO stacks.

## Concepts practiced
- FIFO vs LIFO ordering
- Guarding empty-queue operations (`dequeue`/`front` return `None` with a
  message instead of raising)
- Two-stack queue trick: push everything onto `stack1`; only when `stack2`
  is empty, dump all of `stack1` into `stack2` (which reverses the order),
  then pop from `stack2`. Each element only gets moved from stack1 to
  stack2 once in its lifetime, so `enqueue` is O(1) and `dequeue` is O(1)
  amortized even though a single dequeue can occasionally trigger an O(n)
  transfer.

## How to run
```
python queue_implementation.py
```
Runs both demos: the list-based queue with enqueue/dequeue/front/size checks,
then the two-stack queue showing enqueue/dequeue interleaved to confirm FIFO
order is preserved.

## Status
Complete.
