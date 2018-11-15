# Узник замка Иф

a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
size = d * e
blocks_size = 2 * a * b + 2 * b * c + 2 * a * c
if (size < blocks_size):
    print('NO')
else:
    print('YES')
