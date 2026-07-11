# singly_linked_list .py

from node import Node # Import the Node class from node .py

class SinglyLinkedList :
    def __init__ ( self ):
        self . head = None     # empty lsit head points to nothing 

    def is_empty ( self ):
        if self.head == None:     # checks if the head is none, the list is empty
            return True
        return False
    
    def append (self, data):
        new_node = Node(data)
        
        if self.is_empty():        # if list is emoty make this head
            self.head = new_node
            return
        
        current = self.head   # append at end
        while current.next != None:
            current = current.next
        
        current.next = new_node
        
    def insert (self, index, data):
        if index < 0 :             # if the index is negative
            print("Invald index.")
            return 
        
        new_node = Node(data)
        
        if index == 0:      # insrat at head
            new_node.next = self.head
            self.head = new_node
            return 
        
        current = self.head 
        i = 0 
        while i < index - 1:
            if current == None :
                print ("Index out of range.")
                return
            current = current.next
            i += 1
            
        if current == None:
            print ("Index out of range.")
            
        new_node.next = current.next
        current.next = new_node
    
    def pop(self, index = None):
        if self.is_empty():
            print ("Can't pop from empty list.")
            return None 
        
        if index == None:     # remove the last element 
            if self.head.next == None:        # only one element in list
                val = self.head.data
                self.head = None 
                return val
             
            current = self.head
            while current.next.next != None:
                current = current.next
                
            val = current.next.data
            current.next = None         # remove the last node
            return val
        
        # remove the head 
        if index == 0 :
            val = self.head.data
            self.head = self.head.next
            return val
        
        current = self.head
        i = 0 
        while i < index -1:
            if current.next == None:
                print("Index out of range.") 
                return None 
            current = current.next
            i += 1
        
        if current.next == None: # if we reach end
            print ("Index out of range.")
            return None 
        
        val = current.next.data
        current.next = current.next.next   # skip the node
        return val 
    
            
    def remove_at_index(self , index):
        if self.is_empty():
            print("list is empty.")
            return 
        
        if index < 0 :
            raise IndexError("Index cann't be nagative.")
        
        if index == 0:     # remove head
            self.head = self.head.next
            return 
        
        current = self.head
        i = 0
        while i < index -1:
            if current.next == None:
                raise IndexError("Index out of range.")
            current = current.next
            i +=1
        
        if current.next == None:
            raise IndexError("Index out of range.")
        
        current.next = current.next.next # skip the node
        
    def search(self , data):
        current = self.head
        index = 0
        while current != None:
            if current.data == data:
                return index # return index
            current = current.next
            index += 1
            
        return -1  # return -1 if not found
    
    def display(self):
        current = self.head
        elements = []
        
        while current != None:
            elements.append (str( current.data))
            current = current.next
        elements.append("None")
        
        print (" -> ".join (elements))
    
# Driver / Testing Program

if __name__ == "__main__":
    linked_list = SinglyLinkedList ()
    
        # --- Append ---
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)
    linked_list.display()
    # Expected : 10 -> 20 -> 30 -> 40 -> 50 -> None

    # --- Insert ---
    linked_list.insert(0, 5) # Insert at beginning
    linked_list.display()
    # Expected : 5 -> 10 -> 20 -> 30 -> 40 -> 50 -> None

    linked_list.insert(3, 25) # Insert in the middle
    linked_list.display()
    # Expected : 5 -> 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> None

    # --- Search ---
    pos = linked_list.search(25)
    print ("25 found at index :", pos) # Expected : 3

    pos = linked_list.search (99)
    print ("99 found at index :", pos) # Expected : -1        
                    
    # --- Pop ---
    val = linked_list.pop() # Remove last node
    print (" Popped :", val)
    linked_list.display()

    # --- Remove at index ---

    linked_list.remove_at_index(0) # Remove head
    linked_list.display()

    # --- is_empty ---

    print (" Is empty ?", linked_list.is_empty()) # Expected : False
            
#####################################
# Test the following edge cases:
######################################

    print("Edge case 1: Call pop() on an empty list — what should happen?")   
    empty = SinglyLinkedList()
    empty.pop()
    
    print ("Edge case 2: Call insert(-1, 99) — how should you handle a negative index?")    
    linked_list.insert(-1, 99)
    
    print ("Edge case 3: Call remove at index(100) on a 3-node list — handle gracefully.")
    case3 = SinglyLinkedList()
    case3.append(1)
    case3.append(2)
    case3.append(3)
    case3.display()
    try:
        case3.remove_at_index(100)
    except IndexError as e:
        print ("Index error:" , e)
    case3.display() # list rmains same after error
