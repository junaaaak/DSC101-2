class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def traverse(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr:
            print(itr.data, end=" --> ")
            itr = itr.next
        print("None")

    def search(self, value):
        if self.head is None:
            print("Linked list is empty")
            return None

        index = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1
        return None


if __name__ == "__main__":
    linked_list = LinkedList()
    while True:
        print("\nLinked List Operations:")
        print("1. Display")
        print("2. Insert at beginning")
        print("3. Insert at end")
        print("4. Insert at a certain index")
        print("5. Traverse")
        print("6. Search")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            linked_list.traverse()
        elif choice == 2:
            data = input("Enter data to insert at the beginning: ")
            linked_list.insert_at_beginning(data)
        elif choice == 3:
            data = input("Enter data to insert at the end: ")
            linked_list.insert_at_end(data)
        elif choice == 4:
            index = int(input("Enter the index to insert at: "))
            data = input("Enter data to insert: ")
            linked_list.insert_at(index, data)
        elif choice == 5:
            linked_list.traverse()
        elif choice == 6:
            value = input("Enter the value to search: ")
            index = linked_list.search(value)
            if index is not None:
                print(f"Value found at index: {index}")
            else:
                print("Value not found in the linked list")
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")
