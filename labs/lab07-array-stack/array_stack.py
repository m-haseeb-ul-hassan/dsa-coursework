########################################
# DSA - Lab 07                         #
# Arrays and Stack Implementation      #
########################################


# Q1. Array Using Python List

class Array:
    def __init__(self):
        self.arr = []

    def insert(self, index, value):
        self.arr.insert(index, value)

    def delete(self, index):
        if index < 0 or index >= len(self.arr):
            print("Index out of range")
            return
        self.arr.pop(index)

    def search(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                return i
        return -1

    def update(self, index, value):
        if index < 0 or index >= len(self.arr):
            print("Index out of range")
            return
        self.arr[index] = value

    def display(self):
        print(self.arr)

    def size(self):
        return len(self.arr)


# Q2. Stack Using Python List

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Q3. Find Maximum Element in an Array
# Time Complexity: O(n) - single pass, one comparison per element

def find_max(arr):
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum


# Q4. Reverse an Array Using Stack
# Time Complexity: O(n) - one push pass + one pop pass, both O(n)

def reverse_array(arr):
    stack = []
    for item in arr:
        stack.append(item)

    reversed_arr = []
    while len(stack) > 0:
        reversed_arr.append(stack.pop())

    return reversed_arr


if __name__ == "__main__":
    # --- Array demo ---
    a = Array()
    a.insert(0, 10)
    a.insert(1, 20)
    a.insert(2, 30)
    a.insert(3, 40)
    a.insert(4, 50)
    a.display()                       # [10, 20, 30, 40, 50]

    idx = a.search(30)
    print("Index:", idx)              # Index: 2

    a.update(2, 99)
    a.display()                       # [10, 20, 99, 40, 50]

    a.delete(1)
    a.display()                       # [10, 99, 40, 50]
    print(a.size())                   # 4

    print()

    # --- Stack demo ---
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.peek())                   # 30
    print(s.pop())                    # 30
    print(s.pop())                    # 20
    print(s.size())                   # 1
    print(s.is_empty())               # False
    print(s.pop())                    # 10
    print(s.is_empty())               # True
    s.pop()                           # Stack is empty

    print()

    # --- find_max demo ---
    numbers = [5, 12, 8, 20, 3]
    print("Maximum element:", find_max(numbers))     # 20

    # --- reverse_array demo ---
    arr = [1, 2, 3, 4, 5]
    print("Reversed array:", reverse_array(arr))     # [5, 4, 3, 2, 1]
