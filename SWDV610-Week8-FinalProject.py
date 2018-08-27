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
 
students = Queue()
#put items at the end of the queue
for x in range(int(input("How many students are in your class? "))):
    students.enqueue("Student# " + str(x))

x=(int(input("Are you ready to select a student helper? If Yes, type 1. If No, type 0. ")))
if x==1:
    while True:
        studentCount =int(input("How many student helpers do you need? (Type -1 to quit) "))
        if studentCount==-1:
            break
        else:
            for i in range(studentCount):
                print(students.dequeue())
                
'''Test cases:
-different #s of students in class
-Are you ready? - test 1 and 0. If 1, continues. If 0, program quits.
-How many student helpers? - Test giving -1 as first. Should result in program quit.
                        -Test different #s and test giving -1 after giving different #s.
                        Giving -1 at any time should still quit.
'''