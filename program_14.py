
import pickle
import shelve


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Create objects
s1 = Student("Nikhil", 101, 85)
s2 = Student("Rahul", 102, 90)

students = [s1, s2]

# Serialize objects using pickle
with open("students.pkl", "wb") as file:
    pickle.dump(students, file)

print("Objects saved using pickle.")

# Deserialize objects using pickle
with open("students.pkl", "rb") as file:
    loaded_students = pickle.load(file)

print("\nObjects restored using pickle:")
for student in loaded_students:
    student.display()
    print()

# Store objects using shelve
with shelve.open("student_data") as db:
    db["student1"] = s1
    db["student2"] = s2

print("Objects saved using shelve.")

# Restore objects using shelve
with shelve.open("student_data") as db:
    print("\nObjects restored using shelve:")
    db["student1"].display()
    print()
    db["student2"].display()
