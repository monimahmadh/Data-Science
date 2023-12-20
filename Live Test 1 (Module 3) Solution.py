class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def Display(self):
        print("Name:",self.name, "\nRoll:",self.roll_no)


John = Student("John", 2)
John.Display()
