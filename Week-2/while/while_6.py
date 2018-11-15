# Утренняя пробежка

X = float(input())
Y = float(input())
days = 1
while X < Y:
    X = X + X * 0.1
    days += 1
print(days)
