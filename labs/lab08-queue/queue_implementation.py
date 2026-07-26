########################################
# DSA - Lab 08                         #
# Queue Implementation                 #
########################################


# Q1. Queue Using Python List (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty :(")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is Empty :(")
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Q2. Queue Using Two Stacks
# enqueue() is always O(1) since it only pushes onto stack1.
# dequeue() only pays the transfer cost when stack2 is empty; each
# element is moved from stack1 to stack2 exactly once over its lifetime,
# so the amortized cost per dequeue is still O(1).

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []   # for enqueue
        self.stack2 = []   # for dequeue

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is Empty :(")
            return None
        return self.stack2.pop()


if __name__ == "__main__":
    # --- Q1 demo ---
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    print(f"Front: {q.front()}")              # Front: 10
    print(f"Dequeue: {q.dequeue()}")          # Dequeue: 10
    print(f"Dequeue: {q.dequeue()}")          # Dequeue: 20
    print(f"Size: {q.size()}")                # Size: 3
    print(f"Empty?? {q.is_empty()}")          # Empty?? False

    print()

    # --- Q2 demo ---
    # Why this works: stack1 holds items in insertion order (LIFO on top).
    # When stack1 is dumped into stack2, the order reverses, so the oldest
    # item ends up on top of stack2 and pops first - giving FIFO behaviour.
    qs = QueueUsingStacks()
    qs.enqueue(10)
    qs.enqueue(20)
    qs.enqueue(30)
    print(qs.dequeue())     # 10
    print(qs.dequeue())     # 20
    qs.enqueue(40)
    print(qs.dequeue())     # 30
    print(qs.dequeue())     # 40
