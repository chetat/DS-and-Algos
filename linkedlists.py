# A simple node
class Node:
    # Create initialize node
    def __init__(self, value, next_node):
        self.next = next_node
        self.data = value
    
    def get_data(self):
        return str(self.data)
    
    def set_data(self, value):
        self.data = value
    



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    # Insert Node at the begining of linkedlist
    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.count += 1

        if self.count == 1:
            self.tail = self.head

    def insert_mid(self):
        pass

    def append(self):
        pass

    def delete(self):
        pass

    def get_size(self):
        return f"{self.count} Items"

    def find(self):
        pass

    def print_list(self):
        while(self.head != None):
            print(self.head.data)
            self.head = self.head.next
        if (self.head == None):
            print("Emptied linkedlist")

first_node = 45

midle_node = 5

third_node = {"name": "wilfred"}

last_node = Node(56, None)
linkedlist = LinkedList()
linkedlist.insert(first_node)
linkedlist.insert(midle_node)
linkedlist.insert(third_node)



print(linkedlist.get_size())
linkedlist.print_list()
