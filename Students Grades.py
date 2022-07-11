n = int(input())
students = {}

for data in range(n):
    student,grade = input().split()
    float_grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(float_grade)

for data in students.items():
    print(f"{data[0]} -> {' '.join([f'{x:.2f}' for x in data[1]])} (avg: {(sum(data[1]) / len(data[1])):.2f})")
