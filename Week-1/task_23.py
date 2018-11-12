# Maximum of 2

A = int(input())
B = int(input())
C = (A - B) ** 2
C = C ** (1/2)
max = (A + B + C) / 2
print(int(max))
