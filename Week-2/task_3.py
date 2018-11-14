# Максимум трех чисел

A = int(input())
B = int(input())
C = int(input())
if A > B:
    max = A
else:
    max = B
if C > max:
    max = C
print(max)
