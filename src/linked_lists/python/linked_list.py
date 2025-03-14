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




'''
bellow is the implementation of geeksforgeeks
'''

"""
# Create a Node class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    # Update node at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = val
        else:
            print("Index not present")

    # Method to remove first node of linked list
    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    # Method to remove last node of linked list
    def remove_last_node(self):
        if self.head is None:
            return

        # If there's only one node
        if self.head.next is None:
            self.head = None
            return

        # Traverse to the second last node
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next

        current_node.next = None

    # Method to remove a node at a given index
    def remove_at_index(self, index):
        if self.head is None:
            return

        if index == 0:
            self.remove_first_node()
            return

        current_node = self.head
        position = 0
        while current_node is not None and current_node.next is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None and current_node.next is not None:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    # Method to remove a node from the linked list by its data
    def remove_node(self, data):
        current_node = self.head

        # If the node to be removed is the head node
        if current_node is not None and current_node.data == data:
            self.remove_first_node()
            return

        # Traverse and find the node with the matching data
        while current_node is not None and current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

        # If the data was not found
        print("Node with the given data not found")

    # Print the size of the linked list
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print the linked list
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data:")
llist.printLL()

# remove nodes from the linked list
print("\nRemove First Node:")
llist.remove_first_node()
llist.printLL()

print("\nRemove Last Node:")
llist.remove_last_node()
llist.printLL()

print("\nRemove Node at Index 1:")
llist.remove_at_index(1)
llist.printLL()

# print the linked list after all removals
print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value at Index 0:")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list:", llist.sizeOfLL())
"""