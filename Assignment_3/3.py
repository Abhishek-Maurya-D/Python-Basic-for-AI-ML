list1 = []
list2 = []

n = int(input("Enter the number of elements you want in the list 1: "))
while n>0:
    element = int(input("Enter the element:"))
    list1.append(element)
    n -= 1

m = int(input("Enter the number of elements you want in the list 2: "))
while m>0:
    element = int(input("Enter the element:"))
    list2.append(element)
    m -= 1

list1.sort()
list2.sort()

list = list1 + list2
list.sort()
print("Concatinated list is : ", list)