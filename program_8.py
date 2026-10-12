
def calculate_statistics(*grades):
    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    return minimum, maximum, average


def calculate_grade(**students):
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        distribution[grade] += 1
        print(name, ":", marks, "->", grade)

    return distribution


# Using *args
minimum, maximum, average = calculate_statistics(85, 92, 76, 88, 95)

print("\nMinimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Average Marks:", round(average, 2))

# Using **kwargs
print("\nStudent Grades:")
result = calculate_grade(
    Rahul=92,
    Aman=85,
    Priya=76,
    Neha=65,
    Rohit=45
)

print("\nGrade Distribution:", result)