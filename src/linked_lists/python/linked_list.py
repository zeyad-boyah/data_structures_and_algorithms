'''

insertAtEnd(): Inserts a node at the end of the linked list.
remove_node(): Deletes a node by taking data as an argument. It traverses the linked list and deletes the node if a match is found.
sizeOfLL(): Returns the current size of the linked list.
printLL(): Traverses the linked list and prints the data of each node. printLL() method ensures the last node is printed by adding a print(current_node.data) after the loop ends. This handles the edge case of printing the last node.
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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



# tests
if __name__ == "__main__":
    ll = LinkedList()

    # Test inserting into an empty list at index 0
    ll.insert_at_index(10, 0)  # Expected list: 10

    # Insert at tail (index 1 in a list with 1 element)
    ll.insert_at_index(20, 1)  # Expected list: 10 -> 20

    # Insert in the middle (index 1)
    ll.insert_at_index(15, 1)  # Expected list: 10 -> 15 -> 20

    # Insert at head again
    ll.insert_at_index(5, 0)   # Expected list: 5 -> 10 -> 15 -> 20

    # Attempt to insert at an index that's out-of-bound
    ll.insert_at_index(25, 10) # Expected output: "Index not present"

    # Print final list
    ll.print_list()           # Expected output: 5 -> 10 -> 15 -> 20 -> None

    