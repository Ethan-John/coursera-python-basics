# Коробки

A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
s1 = 2 * A1 * B1 + 2 * B1 * C1 + 2 * A1 * C1
s2 = 2 * A2 * B2 + 2 * B2 * C2 + 2 * A2 * C2
v1 = A1 * B1 * C1
v2 = A2 * B2 * C2
if (s1 == s2):
    print('Boxes are equal')
elif (s1 > s2 and v1 > v2):
    print('The first box is larger than the second one')
else:
    print('The first box is smaller than the second one')
