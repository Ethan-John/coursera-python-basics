# Количество элементов, равных максимуму

N = int(input())
max = N
k = 0
while N != 0:
    if N > max:
        max = N
        k = 1
    elif N == max:
        k += 1
    N = int(input())
print(k)
