class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Append node at the end (similar to insert_at_end)
    def append_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Delete a node with a specific value
    def delete_node(self, data):
        current = self.head
        # If the node to be deleted is the head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        prev = None
        # Search for the node to be deleted
        while current and current.data != data:
            prev = current
            current = current.next

        # If the node was not found
        if current is None:
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Search for a node with specific data
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True  # Node found
            current = current.next
        return False  # Node not found

    # Display the entire linked list
    def display_list(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()

# Example usage
linked_list = LinkedList()

# Append nodes to the list
linked_list.append_node(10)
linked_list.append_node(20)
linked_list.append_node(30)
linked_list.append_node(40)

# Display the list
print("Linked list:")
linked_list.display_list()

# Search for a node in the list
print("Is 30 in the list?", linked_list.search_node(30))  # Expected: True
print("Is 50 in the list?", linked_list.search_node(50))  # Expected: False

# Delete a node
linked_list.delete_node(20)
print("\nLinked list after deleting 20:")
linked_list.display_list()

# Delete a node that doesn't exist
linked_list.delete_node(100)
print("\nLinked list after trying to delete 100 (non-existing):")
linked_list.display_list()

