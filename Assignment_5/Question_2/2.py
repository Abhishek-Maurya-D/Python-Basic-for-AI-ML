data = True;

with open("log.txt", "a+") as f:
    f.write("Program run successfully.");
    f.seek(0);
    while data:
        data = f.readlines();
        print(data);