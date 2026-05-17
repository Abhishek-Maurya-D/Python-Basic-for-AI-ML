class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name);
        self.set_roll_no(roll_no);
        self.set_marks(marks);

    # Getter Methods
    def get_name(self):
        return self.__name;

    def get_roll_no(self):
        return self.__roll_no;

    def get_marks(self):
        return self.__marks;

    def set_name(self, name):
        if name.strip() == "":
            print("Error: Name cannot be empty!");
        else: 
            self.__name = name;

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no;
        else:
            print("Error: Roll No must be between 1 and 100!");

    def set_marks(self, marks):
        if marks < 0:
            print("Error: Marks cannot be negative!");
        else:
            self.__marks = marks;

# Example
s1 = Student("Abhishek", 12, 88)

print(s1.get_name())
print(s1.get_roll_no())
print(s1.get_marks())
