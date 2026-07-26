# main .py

from bst import BST

def main():
    tree = BST()

    tree.insert(10)
    tree.insert(5)
    tree.insert(20)
    tree.insert(15)
    tree.insert(30)

    print("Inorder Traversal:")
    tree.inorder()

    print("\n Searching for 15:", tree.search(15))
    print("Searching for 100: ", tree.search(100))

    print (" Inorder after deletion :")
    tree.inorder()

if __name__ == "__main__":
    main ()
