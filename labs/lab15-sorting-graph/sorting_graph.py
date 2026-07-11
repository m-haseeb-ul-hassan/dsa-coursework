# Task 1 — Bubble Sort: Detect Top 3 Highest Marks

def bubble_sort(marks):
    n = len(marks)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if marks[j] > marks[j+ 1]:
                marks[j] , marks[j + 1] = marks[j + 1], marks[j]
                swapped = True
        if swapped == False:
            break
    return marks

n = int(input("Enter numbers of Student:"))
marks = list(map(int , input("Enter marks : ").split()))

sorted_marks = bubble_sort(marks)
top3 = sorted_marks[-3:]
top3.reverse()

print("Sorted Marks :", *sorted_marks, "Top 3:", *top3)

# Task 2 — Insertion Sort: Sort Names Alphabetically

    
def insertion_sort(names):
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1

        while j >= 0 and names[j] > key:
            names[j +1] = names[j]
            j -= 1
        names[j + 1] = key

        
        print("After inserting", key, ":", *names)
    print("Final :", *names)

n2 = int(input("Enter number of names : "))
names = input("Enter names : ").split()
insertion_sort(names)


# Task 3 — Implement Graph Using Adjacency Matrix


from collections import deque

class GraphMatrix:

    def __init__(self, n):
        self.n = n
        self.mat = [[0]*n for _ in range(n)]

    def add_edge(self, u, v):
        self.mat[u][v] = 1
        self.mat[v][u] = 1

    def remove_edge(self, u, v):
        self.mat[u][v] = 0
        self.mat[v][u] = 0

    def display(self):
        for row in self.mat:
            print(row)

    def add_vertex(self):
        for row in self.mat:
            row.append(0)
        self.n += 1
        self.mat.append([0]*self.n)

    def remove_vertex(self, v):
        self.mat.pop(v)
        for row in self.mat:
            row.pop(v)
        self.n -= 1

    # Task 4 — BFS Traversal (Using Adjacency Matrix)
    def bfs(self, start):
        visited = [False]*self.n
        queue = deque()
        visited[start] = True
        queue.append(start)

        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for i in range(self.n):
                if self.mat[node][i] == 1 and visited[i] == False:
                    visited[i] = True
                    queue.append(i)

        print("BFS :", *result)

g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(0, 3)

g.display()
g.bfs(0)
