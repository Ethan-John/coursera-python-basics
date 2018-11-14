# Шашки

c1 = int(input())
r1 = int(input())
c2 = int(input())
r2 = int(input())
if ((c2 - c1) % 2 == (r2 - r1) % 2):
    print('YES')
else:
    print('NO')
