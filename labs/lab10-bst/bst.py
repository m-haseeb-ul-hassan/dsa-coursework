from bst_node import BSTNode

class BST:
    def __init__ ( self ) :
        self.root = None
        self.size = 0


    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left , key)
        elif key > node.key:
            node.right = self._insert(node.right , key)
        return node
               
    def insert (self, key):
           self.root = self._insert(self.root , key)
           self.size += 1

    def _search(self, node , key):
        if node is None:
            return False
        if node.key == key:
              return True
        
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right , key)
    
    def search (self, key):
        return self._search (self.root, key)
    
     
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.key , end = " ")
            self._inorder(node.right)
    
    def inorder(self):
        self._inorder(self.root)
        print()

    def _preorder(self, node):
        if node is not None:
            print(node.key, end= "")
            self._preorder(node.left)
            self._preorder(node.right)
        
    def preorder(self):
        self._preorder(self.root)
        print()


    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print (node.key , end =" ")
        
    def postorder(self):
        self._postorder(self.root)
        print()

