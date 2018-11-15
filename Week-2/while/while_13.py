# Количество элементов, больше предыдущего

N = float(input())
k = 0
while N != 0:
    N2 = N
    N = float(input())
    if N > N2:
        k += 1
print(k)
