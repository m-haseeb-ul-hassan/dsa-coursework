
from bst_node import BSTNode

class BST:
    def __init__(self):
        self.root = None
     
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
   
        else:
            self._insert_helper(self.root, key)

    def _insert_helper(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            
            else:
                self._insert_helper(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
             
            else:
                self._insert_helper(node.right, key)


    def search(self, key):
        return self._search_helper(self.root, key)

    def _search_helper(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        elif key < node.key:
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)

    def inorder(self):
        self._inorder_helper(self.root)
        print()  

    def _inorder_helper(self, node):
        if node is not None:
            self._inorder_helper(node.left)
            print(node.key, end=" ")
            self._inorder_helper(node.right)

    def preorder(self):
        self._preorder_helper(self.root)
        print()

    def _preorder_helper(self, node):
        if node is not None:
            print(node.key, end=" ")
            self._preorder_helper(node.left)
            self._preorder_helper(node.right)

    def postorder(self):
        self._postorder_helper(self.root)
        print()

    def _postorder_helper(self, node):
        if node is not None:
            self._postorder_helper(node.left)
            self._postorder_helper(node.right)
            print(node.key, end=" ")

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        # Empty tree — print "Tree is empty.
        if self.root is None:
            print("Tree is empty.")
            return

        # Also handle:
        # Key not found — print "Key not found."

        if self.search(key) is None:
            print("Key not found.")
            return

        self.root = self._delete_helper(self.root, key)
     

    def _delete_helper(self, node, key):
        if node is None:
            return None

        # go left or right to find the node
        if key < node.key:
            node.left = self._delete_helper(node.left, key)
        elif key > node.key:
            node.right = self._delete_helper(node.right, key)
        else:
            # case 1:  Leaf node: no children. Simply remove it
            if node.left is None and node.right is None:
                return None

            # case 2:  One child: replace the node with its only child.
            elif node.left is None:
                return node.right

            # case 2: 
            elif node.right is None:
                return node.left

            # case 3: Two children: copy the in-order successor’s key into the node,
            # then delete the successor
            else:
                successor = self.find_min(node.right)
                node.key = successor.key
                node.right = self._delete_helper(node.right, successor.key)

        return node