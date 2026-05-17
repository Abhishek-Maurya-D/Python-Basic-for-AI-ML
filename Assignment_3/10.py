string = str(input("Enter the String: "))

set1 = set()
for char in string:
    set1.add(char)

print("All the unique characters are : ", set1)
print("Number of unique characters are : ", len(set1))
