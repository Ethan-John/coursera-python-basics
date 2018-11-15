# Среднее значение последовательности

N = float(input())
k = 0
sum = 0
while N != 0:
    k += 1
    sum += N
    N = float(input())
print(sum/k)
