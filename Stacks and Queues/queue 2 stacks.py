#Implement a queue using two stacks.
#first in first out


class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enQueue(self, item):
        self.stack1.append(item)

    def deQueue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def printQ(self):
        print(self.stack2[::-1] + self.stack1)


queue = queue()
queue.enQueue(4)
queue.enQueue(6)
queue.enQueue(5)
queue.printQ()

queue.deQueue()
queue.printQ()

queue.enQueue(2)
queue.deQueue()
queue.printQ()
