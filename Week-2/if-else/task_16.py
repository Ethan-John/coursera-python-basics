# Сколько совпадает чисел

a, b, c = int(input()), int(input()), int(input())
if (a == b and a == c):
    print(3)
elif ((a == b and a != c) or (b == c and b != a) or (a == c and a != b)):
    print(2)
else:
    print(0)
