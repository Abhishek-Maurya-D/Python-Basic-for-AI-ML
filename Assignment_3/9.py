list1 = [3,2,1,5,6,7,4,3,2,3,5,7,8,6,3,5,3,2,2]
set1 = set(list1) #[1,2,3,4,5,6,7,8]

occurance_dict = {}
for ele in set1:
    count = 0
    for item in list1:
        if ele == item:
            count += 1
    list1.remove(item)
    occurance_dict[ele] = count

for key, value in occurance_dict.items():
    if value > 1:
        print(f"{key}")

print(occurance_dict)