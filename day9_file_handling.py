import statistics

with open("student_data.txt", "w") as file:
    file.write("Kamal, 45\n")
    file.write("Johny, 22\n")
    file.write("Chris, 53\n")

num1 = []
with open("student_data.txt", "r") as file:
    for line in file:
        name, grade = line.split(", ")
        num1.append(int(grade.strip()))
print(statistics.mean(num1))

