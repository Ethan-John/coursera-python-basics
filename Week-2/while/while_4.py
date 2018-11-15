# Точная степень двойки

N = int(input())
i = 1
while i <= N:
    if N == 1 or i == N:
        print('YES')
        break
    i = 2 * i
if i != N:
    print('NO')