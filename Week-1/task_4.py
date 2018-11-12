# Apples-2

students = int(input())
apples = int(input())
if students | apples < 10000:
    print(apples % students)
else:
    print("Количество студентов и яблок должно быть < 10000! Введите повторно:")
    students = int(input())
    apples = int(input())
    print(apples % students)
