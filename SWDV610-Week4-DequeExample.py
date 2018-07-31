class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

#add items to the front of queue    
    def addFront(self, item):
        self.items.append(item)
        return self.items
#add items to rear of queue
    def addRear(self, item):
        self.items.insert(0,item)
        return self.items
        
#remove items from front
    def removeFront(self):
        if len(self.items)>0:
             return self.items.pop()
        else:
            return("Deque is empty.")
        
#remove items from rear
    def removeRear(self):
        if len(self.items)>0:
             return self.items.pop(0)
        else:
            return("Deque is empty.")

    def size(self):
        return len(self.items)

#testing

testDeque = Deque()
print(testDeque.addFront(3))
print(testDeque.addFront(7))
print(testDeque.addRear(6))
print(testDeque.addFront(9))
print(testDeque.addRear(4))
print(testDeque.removeFront())
print(testDeque.removeRear())
print(testDeque.removeRear())
print(testDeque.removeRear())
print(testDeque.removeRear())
print(testDeque.removeRear())