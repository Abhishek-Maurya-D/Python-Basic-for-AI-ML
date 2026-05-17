with open("name.txt", "w") as f:
    for i in range(5):
        name = input("Enter name:");
        f.write(name);
        f.write("\n");

print("Names of the students are: ");

with open("name.txt", "r") as f:
    for i in range(5):
        data = f.readline();
        print(data);