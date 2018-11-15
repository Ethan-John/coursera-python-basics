# Максимум последовательности

N = float(input())
max = N
while N != 0:
    if N == 0:
        break
    N = float(input())
    if N > max:
        max = N
print(int(max))
