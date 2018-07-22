def reverseList(list):
    if len(list) == 0:
        return []
    else:
        return [list.pop()] + reverseList(list)

def main():
    list = input("Please enter a list of numbers: ")
    list = list.split(',')
    list = [int(i) for i in list]
    reverse = reverseList(list)
    reverseListString = ','.join(str(n) for n in reverse)
    print("The number sequence in reverse is: ",reverseListString)   
main()
