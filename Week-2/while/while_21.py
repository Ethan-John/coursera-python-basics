# Максимальное число подряд идущих равных

N = int(input())
counter = 1
max1b1 = 1
while N != 0:
    x = N
    N = int(input())
    if x != N and N != 0:
        counter = 1
    elif x == N:
        counter += 1
        if counter > max1b1:
            max1b1 = counter
print(max1b1)
