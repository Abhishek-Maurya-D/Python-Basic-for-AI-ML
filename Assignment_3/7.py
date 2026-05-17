string = str(input("Enter the sentence : "))
num_space = 0
for i in string:
    if i == ' ':
        num_space += 1
print("Number of spacing in the sentence is : ", num_space)