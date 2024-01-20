#Implement a stack using two queues
#last in first out
from queue import Queue


class stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue1.put(item)
        while not self.queue2.empty():
            new = self.queue2.get()
            self.queue1.put(new)
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        return self.queue2.get()

    def isEmpty(self):
        if self.queue1.empty() and self.queue2.empty():
            return True
        return False

    def printStack(self):
        allItems = list(self.queue1.queue) + list(self.queue2.queue)
        print("Stack:", allItems)


st = stack()
st.push(4)
st.push(6)
st.push(5)
st.printStack()

st.pop()
st.printStack()
