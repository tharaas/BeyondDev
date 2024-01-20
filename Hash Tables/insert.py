#Implement a hash table and write functions to insert, delete, and search for elements.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class hashTable:
    def __init__(self, n):
        self.n = n
        self.size = 0
        self.table = [None] * n

    def insert(self, key, value):
        hashN = hash(key) % self.n

        if self.table[hashN] is None:
            self.table[hashN] = Node(key, value)
            self.size += 1
        else:
            new = self.table[hashN]
            while new:
                if new.key == key:
                    new.value = value
                    return
                new = new.next
            node = Node(key, value)
            node.next = self.table[hashN]
            self.table[hashN] = node
            self.size += 1

    def deleteH(self, key):
        hashN = hash(key) % self.n
        if self.table[hashN] is None:
            return None
        else:
            current = self.table[hashN]
            previous = None
            while current:
                if current.key == key:
                    if previous is None:
                        self.table[hashN] = current.next
                    else:
                        previous.next = current.next
                    self.size -= 1
                    print("\nThe key", key, "is deleted")
                    return
                previous = current
                current = current.next

    def searchH(self, key):
        hashN = hash(key) % self.n
        new = self.table[hashN]
        while new:
            if new.key == key:
                return new.value
            new = new.next
        return None

    def printH(self):
        for index in range(self.n):
            current = self.table[index]
            while current:
                print(current.key, current.value)
                current = current.next


hashT = hashTable(4)
hashT.insert(10, "Apple")
hashT.insert(13, "car")
hashT.insert(2, "lemon")
hashT.insert(8, "dog")
hashT.printH()

val = hashT.searchH(13)
print("The value of 13 is", val)

hashT.deleteH(2)
hashT.printH()
val = hashT.searchH(2)
print("\nThe value of 2 is", val)
