def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1

            alist[position]=currentvalue

alist = [2,5,4,1,7,6,10,8,9,3]
#alist = [1,2,3,4,5,6,7,8,9,10]

insertionSort(alist)
print(alist)