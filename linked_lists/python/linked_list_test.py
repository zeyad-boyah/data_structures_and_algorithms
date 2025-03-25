import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_index(self):
        # Test inserting into an empty list at index 0
        self.ll.insert_at_index(10, 0)
        self.assertEqual(self.ll.to_list(), [10])

        # Insert at tail (index 1 in a list with 1 element)
        self.ll.insert_at_index(20, 1)
        self.assertEqual(self.ll.to_list(), [10, 20])

        # Insert in the middle (index 1)
        self.ll.insert_at_index(15, 1)
        self.assertEqual(self.ll.to_list(), [10, 15, 20])

        # Insert at head again
        self.ll.insert_at_index(5, 0)
        self.assertEqual(self.ll.to_list(), [5, 10, 15, 20])

        # Insert at index 2
        self.ll.insert_at_index(5, 2)
        self.assertEqual(self.ll.to_list(), [5, 10, 5, 15, 20])

        # Attempt to insert at an index that's out-of-bound.
        # This should print "Index not present" and leave the list unchanged.
        self.ll.insert_at_index(25, 10)
        self.assertEqual(self.ll.to_list(), [5, 10, 5, 15, 20])

    def test_remove_node(self):
        # Test removing from an empty list.
        self.ll.remove_node(10)
        self.assertEqual(self.ll.to_list(), [])

        # Test removing the head node.
        self.ll.add_to_head(10)  # List: 10
        self.ll.add_to_head(20)  # List: 20 -> 10
        self.ll.add_to_head(30)  # List: 30 -> 20 -> 10
        self.ll.remove_node(30)  # Remove head (30)
        self.assertEqual(self.ll.to_list(), [20, 10])

        # Test removing a middle node.
        self.ll.insert_at_end(40)  # List becomes: 20 -> 10 -> 40
        self.ll.remove_node(10)    # Remove the middle node (10)
        self.assertEqual(self.ll.to_list(), [20, 40])

        # Test removing the tail node.
        self.ll.insert_at_end(50)  # List becomes: 20 -> 40 -> 50
        self.ll.remove_node(50)    # Remove tail (50)
        self.assertEqual(self.ll.to_list(), [20, 40])

        # Test removing a non-existent node.
        self.ll.remove_node(100)   # Expect "Node not found"
        self.assertEqual(self.ll.to_list(), [20, 40])

if __name__ == '__main__':
    unittest.main()
