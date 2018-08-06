def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

alist = [2,5,4,1,7,6,10,8,9,3]
#alist = [1,2,3,4,5,6,7,8,9,10]

selectionSort(alist)
print(alist)