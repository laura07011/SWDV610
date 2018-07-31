class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

#add items to queue
    
    def enqueue(self, item):
        self.items.insert(0,item)
        return self.items

#remove items from queue in FIFO order
    def dequeue(self):
        if len(self.items)>0:
             return self.items.pop()
        else:
            return("Queue is empty.")

    def size(self):
        return len(self.items)

#testing

testQueue = Queue()
print(testQueue.enqueue(3))
print(testQueue.enqueue(7))
print(testQueue.enqueue(6))
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())