# Количество четных элементов последовательности

N = float(input())
k = 0
while N != 0:
    if N % 2 == 0:
        k += 1
    N = float(input())
print(k)
