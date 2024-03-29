import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")


def sorting(linked_list):
    values = []
    current = linked_list.head
    while current:
        values.append(current.data)
        current = current.next

    sorted_values = insert_sort(values)

    linked_list = LinkedList()
    for i in sorted_values:
        linked_list.append(i)

    return linked_list


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sorting_by_head(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head

    while current is not None:
        next_node = current.next
        sorted_head = insert_sort_by_head(sorted_head, current)
        current = next_node

    return sorted_head

def insert_sort_by_head(head, new_node):
    if head is None or head.data >= new_node.data:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.data < new_node.data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head

def reverse(linked_list):
    current = linked_list.head
    prev = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev
    return linked_list


def merge(list1, list2):
    merged_list = LinkedList()

    current1 = list1
    current2 = list2

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list

def print_by_head(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


def init_list(list):
    for i in range(0, 10):
        list.append(random.randint(1, 50))
    return list


def main():
    linked_list1 = LinkedList()
    linked_list1 = init_list(linked_list1)

    linked_list2 = LinkedList()
    linked_list2 = init_list(linked_list2)

    linked_list3 = LinkedList()
    linked_list3 = init_list(linked_list3)

    print("\nHаписати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами")
    print("Початковий список:")
    linked_list3.display()
    print("Реверсивний список:")
    reversed_list = reverse(linked_list3)
    reversed_list.display()

    print("\n\nРозробити алгоритм сортування для однозв'язного списку, сортування вставками")
    print("Початковий список:")
    linked_list1.display()
    print("Сортований список:")
    linked_list1_head = sorting_by_head(linked_list1.head)
    print_by_head(linked_list1_head)

    print("\n\nНаписати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список")
    print("Початковий список:")
    print_by_head(linked_list1_head)
    linked_list2_head = sorting_by_head(linked_list2.head)
    print_by_head(linked_list2_head)

    print("Зʼєднаний список:")
    merged_list = merge(linked_list1_head, linked_list2_head)
    merged_list.display()


if __name__ == "__main__":
    main()
