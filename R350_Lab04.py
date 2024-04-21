class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data, index=None):
        if index is None or index == 0:
            node = Node(data, self.head)
            self.head = node
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def delete_at_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def delete_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.delete_at_beginning()
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
        print("2. Create/Add a node")
        print("3. Delete at beginning")
        print("4. Delete at end")
        print("5. Delete at a certain index")
        print("6. Traverse")
        print("7. Search")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            linked_list.traverse()
        elif choice == 2:
            data = input("Enter data to insert: ")
            index = int(input("Enter the index to insert at (optional, leave empty for beginning): ") or 0)
            linked_list.add(data, index)
        elif choice == 3:
            linked_list.delete_at_beginning()
        elif choice == 4:
            linked_list.delete_at_end()
        elif choice == 5:
            index = int(input("Enter the index to delete: "))
            linked_list.delete_at(index)
        elif choice == 6:
            linked_list.traverse()
        elif choice == 7:
            value = input("Enter the value to search: ")
            index = linked_list.search(value)
            if index is not None:
                print(f"Value found at index: {index}")
            else:
                print("Value not found in the linked list")
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")