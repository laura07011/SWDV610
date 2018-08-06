def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [2,5,4,1,7,6,10,8,9,3]
#alist = [1,2,3,4,5,6,7,8,9,10]

bubbleSort(alist)
print(alist)