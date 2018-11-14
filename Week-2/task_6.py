# Квартиры

A = int(input())
B = int(input())
N = B - A + 1
if (A >= 1):
    if (B % N == 0):
        print('YES')
    else:
        print('NO')
