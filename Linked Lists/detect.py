# Write a program to detect if a linked list has a cycle.


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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detect(self):
        newList = set()
        temp = self.head
        while temp:
            if temp in newList:
                return True
            newList.add(temp)
            temp = temp.next
        return False


list = LinkedList()
list.push(98)
list.push(45)
list.push(2)

if list.detect():
    print("The linked list is cycle")
else:
    print("The linked list is not cycle")
    list.printList()

print("\n")

list2 = LinkedList()
list2.push(98)
list2.head.next = list2.head

if list2.detect():
    print("The linked list is cycle")
else:
    print("The linked list is not cycle")
    list2.printList()
