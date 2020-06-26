class Node:
    def __init__(self, value, next_node):
        self.next = next_node
        self.data = value
   

class LinkedList:
    def __init__(self, head, node):
        pass

    def insert(self):
        pass

    def insert_mid(self):
        pass

    def append(self):
        pass

    def delete(self):
        pass 



first_node = Node(5, None)

midle_node = Node(8, None)

last_node = Node(56, None)

first_node.next = midle_node

midle_node.next = last_node

def print_nodes(node):
    while(node != None):
        print(node.data)
        node = node.next


print_nodes(first_node)