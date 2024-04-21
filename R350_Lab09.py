def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def print_menu():
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quit")

while True:
    print("\nMenu:")
    print_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        bubble_sort(arr)
        print("Sorted array:", arr)
    elif choice == '2':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        selection_sort(arr)
        print("Sorted array:", arr)
    elif choice == '3':
        arr = list(map(int, input("Enter space-separated integers: ").split()))
        insertion_sort(arr)
        print("Sorted array:", arr)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
