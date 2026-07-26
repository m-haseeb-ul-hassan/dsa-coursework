# library .py

from bst import BST

class Book:
    def __init__(self , isbn , title , author):
        self.isbn = isbn 
        self.title = title 
        self.author = author 
    
    def __str__(self):
        return f"{self.isbn} | {self.title} | {self.author}"

class LibraryCatalogue:
    def __init__(self):
        self.tree = BST()
        self.books = {}

    def add_book(self, isbn, title, author):
        b = Book(isbn, title, author)
        self.books[isbn] = b
        self.tree.insert(isbn)

    def remove_book(self, isbn):
        if isbn not in self.books:
            print(f"Removing {isbn}... Not found.")
            return
        print(f"Removing {isbn}... done.")
        self.tree.delete(isbn)
        del self.books[isbn]

    def find_book(self, isbn):
        result = self.tree.search(isbn)
        if result is None:
            print(f"Searching {isbn}: Not found.")
        else:
            print(f"Searching {isbn}: {self.books[isbn]}")

    def list_all(self):
        # collect keys in sorted order using inorder traversal
        sorted_keys = []
        self._collect_inorder(self.tree.root, sorted_keys)
        for isbn in sorted_keys:
            print(self.books[isbn])

    def _collect_inorder(self, node, result):
        if node is not None:
            self._collect_inorder(node.left, result)
            result.append(node.key)
            self._collect_inorder(node.right, result)


def main():
    catalogue = LibraryCatalogue()

    # add the 5 books
    catalogue.add_book(10, "pythoin", "Ali")
    catalogue.add_book(11, "The python", "Huzaifa")
    catalogue.add_book(1540, "intro to python", "huzaifa")
    catalogue.add_book(510, "Structure and Interpretation", "Abelson & Sussman")
    catalogue.add_book(12, "Design Patterns", "Gang of Four")

    print("All Books")
    catalogue.list_all()

    catalogue.find_book(12)   # should be found
    catalogue.find_book(9999)   # should not be found

    catalogue.remove_book(11)  # lost copy
    catalogue.remove_book(10) # withdrawn

    print("Remaining Books")
    catalogue.list_all()


if __name__ == "__main__":
    main()
        