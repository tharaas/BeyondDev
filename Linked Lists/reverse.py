# Write a program to reverse a linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


list = LinkedList()
list.push(98)
list.push(45)
list.push(2)

print("The list")
list.printList()
list.reverse()
print("\nReversed linked list")
list.printList()
