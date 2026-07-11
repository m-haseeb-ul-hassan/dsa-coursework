# node.py
#  This file defines the Node class used in the linked list .

class Node:
    def __init__(self, data):
        self.data = data     # srorest he value
        self.next = None  # Points to the next node ( None by default )


if __name__ == "__main__":
                
    # 2. Manually create two Node objects in a Python shell and link them together using .next.
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2

    # 3. Print node1.data and node1.next.data to verify the link works correctly
    print (node1.data)
    print (node1.next.data)
