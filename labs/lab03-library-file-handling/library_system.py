################################# 
# Lab 3 - OOP & File Handling   #
##########################################################
# Library Management System using OOP and File handling  #
##########################################################

# 1. Class 1: Book

class Book:
    def __init__(self, book_ID , title , author , status = "Available"):
        self.__book_ID = book_ID
        self.__title = title
        self.__author = author 
        self.__status = status 

    def get_Book_ID (self):
        return self.__book_ID
    
    def get_title (self):
        return self.__title
    
    def get_author (self):
        return self.__author
    
    def get__status(self ):
        return self.__status

    def issue_book (self):
        if self.__status == "Available":
            self.__status = "Issued"
            return True
        return False

    def display (self):
        print (f"Book ID: {self.__book_ID}\n Title: {self.__title}\n Author of Book: {self.__author}\n Status: {self.__status}\n Thanks.")

    def to_file_string(self):
        return f"{self.__book_ID} , {self.__title} , {self.__author} , {self.__status}\n"
    
class Library:
    def __init__(self, fileName = "book.txt"):
        self.fileName = fileName

    def add_book(self , book):
        with open(self.fileName , "a") as file:
            file.write (book.to_file_string())
        print ("Successfully Added Book!!!\nThanks.")

    def view_books (self):
        try:
            with open (self.fileName , "r") as file:
                lines = file.readlines()
                if len (lines) == 0:
                    print ("No Books Available!!!\nThanks.")
                else :
                    for line in lines:
                        data = line.strip().split(",")
                        book = Book(data[0].strip() , data[1].strip() , data[2].strip() , data[3].strip())
                        book.display()
        except FileNotFoundError:
            print ("No Books Available :)\nThanks.")

    def issue_book( self , book_ID):
        try:
            with open (self.fileName , "r") as file:
                lines = file.readlines()

            check = False
            with open (self.fileName , "w") as file:
                for line in lines:
                    data = line.strip().split(",")
                    
                    if data [0].strip() == book_ID:
                        check = True

                        if data[3].strip() == "Available":
                            data [3] = "Issued"
                            print ("Successfully Issued Book!!!\nThanks.")
                        else:
                            print ("Book already Issued!!!\nThanks.")
                    file.write (f"{data[0]} ,{data[1]} ,{data[2]} ,{data[3]}\n")
        
            if check == False:
                print ("Book Not Found :)\nThanks.")

        except FileNotFoundError:
            print ("No Books Available :)\nThanks.")
        
    def return_book(self , book_ID):
        try:
            with open (self.fileName , "r") as file:
                lines = file.readlines()

            check = False
            with open (self.fileName , "w") as file:
                for line in lines:
                    data = line.strip().split(",")
                    
                    if data [0].strip() == book_ID:
                        check = True

                        if data[3].strip() == "Issued":
                            data [3] = "Available"
                            print ("Successfully Returned Book!!!\nThanks.")
                        else:
                            print ("Book Not Issued!!!\nThanks.")
                    file.write (f"{data[0]} ,{data[1]} ,{data[2]} ,{data[3]}\n")

            if check == False:
                print ("Book Not Found :)\nThanks.")

        except FileNotFoundError:
            print ("No Books Available :)\nThanks.")

    def search_book (self, book_ID):
        try:
            with open (self.fileName , "r") as file:
                lines = file.readlines()

                for line in lines:
                    data = line.strip().split(",")
                    
                    if data [0].strip() == book_ID:
                        book = Book(data[0].strip() , data[1].strip() , data[2].strip() , data[3].strip())
                        book.display()
                        return
                print ("Book Not Found :)\nThanks.")

        except FileNotFoundError:
            print ("No Books Available :)\nThanks.")

library = Library()

while True:
    print("1. Add Book\n2. View All Books\n3. Issue Book\n4. Return Book\n5. Search Book\n6. Exit")

    choice = int (input ("Please Select an Option:"))

    if choice == 1:
        book_id = input ("Please Enter Book ID:")
        title = input ("Please Enter Title:")
        author = input ("Please Enter Author:")

        book = Book (book_id , title , author , status = "Available")
        library.add_book(book)

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        book_id = input ("Please Enter Book Id:")
        library.issue_book(book_id)

    elif choice == 4:
        book_id = input ("Please Enter Book ID:")
        library.return_book(book_id)

    elif choice == 5:
        book_id = input ("Please Enter Book ID:")
        library.search_book(book_id)

    elif choice == 6:
        print ("Exiting...")
        break 
    
    else:
        print ("Try Again, Invalid Choice!!!")
