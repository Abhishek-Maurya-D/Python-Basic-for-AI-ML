class Person():    
    def __init__(self, name, age=None, address=None):
        self.name = name;
        self.age = age;
        self.address = address;

p1 = Person("Abhishek");
p2 = Person("Amit", 21);
p3 = Person("Ankit", 23, "Delhi B64 Goyal Colony");

print(p1.name);
print(p2.age);
print(p3.address);