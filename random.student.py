import random

num_students = int(input("Enter the number of students: "))
sick_students = [(x) for x in input("Enter the sick students : ").split(",")]

students = [(student) for student in range(1, num_students + 1)]

while True:
    ans = input("Do you want to start (y,n): ")
    while ans != "n":
        for student in students:
            random_student = random.choice(student)
            if random_student in sick_students:
                students.remove(random_student)
                continue
            else:
                print(f"Computer chose: {student}")
                students.remove(random_student)
            print(f"The left students are : {students}")
            ans = ("Do you want to continue (y,n): ")