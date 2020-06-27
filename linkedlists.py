# A simple node
class Node:
    # Create initialize node
    def __init__(self, value, next_node=None):
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

    def append(self, data):
        if self.head == None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.tail.next = Node(data, None)


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

first_node = 45
second_node = 5
third_node = {"name": "wilfred"}
fourth_node = [2,5,6]
last_node = (456,12,66)

linkedlist = LinkedList()
linkedlist.insert(first_node)
linkedlist.insert(second_node)
linkedlist.insert(third_node)
linkedlist.append(last_node)
linkedlist.insert(first_node)
linkedlist.print_list()
