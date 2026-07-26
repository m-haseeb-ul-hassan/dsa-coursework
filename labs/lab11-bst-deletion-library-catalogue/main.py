from bst import BST

def main():
    tree = BST()

    for key in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(key)

    print("Inorder before deletion:")
    tree.inorder()       # 20 30 40 50 60 70 80 
 
    tree.delete(20)      # case 1: leaf
    print("\nAfter deleting 20 (leaf):")
    tree.inorder()       # 30 40 50 60 70 80 
 
    tree.delete(30)      # case 2: one child     
    print("\nAfter deleting 30 (one child):")
    tree.inorder()        # 40 50 60 70 80 

    tree.delete(50)       # case 3: two children
    print("\nAfter deleting 50 (two children):")
    tree.inorder() # 40 60 70 80

    tree.delete(99)  # not found 

if __name__ == "__main__":
    main()