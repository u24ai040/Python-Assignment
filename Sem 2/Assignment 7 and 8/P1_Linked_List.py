# QUESTION 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Key not found in the list.")
            return
        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()
while True:
        choice = input("\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter choice: ")
        if choice == '1':
            data = int(input("Enter data to insert: "))
            ll.insert(data)
        elif choice == '2':
            key = int(input("Enter data to delete: "))
            ll.delete(key)
        elif choice == '3':
            ll.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")
