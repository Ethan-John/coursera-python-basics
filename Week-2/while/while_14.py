# Второй максимум

N = int(input())
max1 = N
max2 = N / max1
while N != 0:
    N = int(input())
    if N > max1:
        max1, max2 = N, max1
    elif N > max2 and (N <= max1):
        max2 = N
print(int(max2))
