# Четные и нечетные

A = int(input())
B = int(input())
C = int(input())
is_even = False
is_odd = False
if ((A % 2 == 0) or (B % 2 == 0) or (C % 2 == 0)):
    is_even = True
if ((A % 2 == 1) or (B % 2 == 1) or (C % 2 == 1)):
    is_odd = True
if (is_even == is_odd):
    print('YES')
else:
    print('NO')
