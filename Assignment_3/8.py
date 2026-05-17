list1 = [1,2,3,4]
list2 = [5,2,7,8]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)
if len(intersection) == 0:
    print("No Common Element")
else:
    print("Common Element")