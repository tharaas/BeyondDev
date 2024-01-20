# Write a program to find the middle element of a linked list.


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

    def len(self):
        len0 = 0
        temp = self.head
        while temp:
            len0 += 1
            temp = temp.next
        return len0

    def middleElement(self):
        temp = self.head
        len0 = int(self.len())
        if len0 % 2 != 0:
            len0 = int((len0 + 1)/2)
        for i in range(len0-1):
            temp = temp.next
        print("The middle element is ", temp.data)

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
list.middleElement()
