class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

#add an item to list
        
     def push(self, item):
         self.items.append(item)
         return self.items
         
#remove an item from list
         
     def pop(self):
         if len(self.items)>0:
             return self.items.pop()
         else:
            return("Stack is empty.")

     def size(self):
         return len(self.items)

#testing

testStack = Stack()
print(testStack.push(3))
print(testStack.push(7))
print(testStack.push(6))
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())