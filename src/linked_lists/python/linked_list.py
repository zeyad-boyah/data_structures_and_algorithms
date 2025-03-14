'''
printLL(): 
'''







class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# __init__: Initializes the linked list with an empty head.
class LinkedList():
    def __init__(self):
        self.head = None

    # Inserts a node at the beginning of the linked list.
    def add_to_head(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            pointer = self.head
            self.head = new_node
            new_node.next = pointer

    
    # Inserts a node at the given index of the linked list.
    def insert_at_index(self, data, index:int):
        if  index == 0:
            self.add_to_head(data)
            print("new node inserted")
            return
        new_node = Node(data)
        node_before = None
        current_node = self.head
        linked_list_index = 0
        while True:
            if current_node == None and index > linked_list_index:
                print("index not present")
                return

            if linked_list_index == index:
                node_before.next = new_node
                new_node.next = current_node
                print("new node inserted")
                return 0
            node_before = current_node
            current_node = current_node.next
            linked_list_index += 1

    # insert a node at the end
    def insert_at_end(self, data):
        if self.head == None:
            self.add_to_head(data)
            print("new node inserted")
            return
        current_node = self.head
        while current_node:
            if current_node.next == None:
                new_node = Node(data)
                current_node.next = new_node
                return
            current_node = current_node.next
        

    # Deletes a node by taking data as an argument. It traverses the linked list and deletes the node if a match is found.
    def remove_node(self, data):
        if self.head == None:
            print("can't delete the required node because the LL is already empty")
            return
        
        current_node = self.head
        if current_node.data== data:
            self.head = current_node.next

        while current_node.next:
            node_after = current_node.next
            if node_after.data == data:
                current_node.next = node_after.next
                print("node deleted")
                return
            current_node = current_node.next

    #  Returns the current size of the linked list.
    def size_of_LL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Traverses the linked list and prints the data of each node.
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def to_list(self):
        """Helper method to convert the linked list into a Python list mainly for the unit test."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
