class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} added to the queue.")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"{removed_item} removed from the queue.")
        else:
            print("Queue is empty! Cannot dequeue.")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", " -> ".join(self.items))


queue = Queue()
    
while True:
        print("\nQueue Operations:")
        print("1. Enqueue (Add)")
        print("2. Dequeue (Remove)")
        print("3. Display Queue")
        print("4. Exit")

        choice = input("Choose an option from 1 to 4: ")

        if choice == '1':
            item = input("Enter the element to enqueue: ")
            queue.enqueue(item)

        elif choice == '2':
            queue.dequeue()

        elif choice == '3':
            queue.display()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")
