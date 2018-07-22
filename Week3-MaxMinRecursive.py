def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        newMax = Max(list[1:])
        max = list[0]
        if newMax > max:
            return newMax
        else:
            return max

def Min(list):
    if len(list) == 1:
        return list[0]
    else:
        newMin = Min(list[1:])
        min = list[0]
        if newMin < min:
            return newMin
            newMin = min
        else:
            return min
        
def main():
    list = input("Please enter a list of numbers: ")
    list = list.split(',')
    list = [int(i) for i in list]
    print("The maximum number is: ", Max(list))
    print("The minimum number is: ", Min(list))

main()