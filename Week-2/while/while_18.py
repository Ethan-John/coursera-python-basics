# Исполнитель раздвоитель

A = int(input())
B = int(input())

while A != B:
    if A % 2 == 0 and A >= B * 2:
        A = A / 2
        print(':2')
    elif A != B:
        A = A - 1
        print('-1')
