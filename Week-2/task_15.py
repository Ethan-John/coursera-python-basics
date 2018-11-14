# Упорядочить три числа

a, b, c = int(input()), int(input()), int(input())
if (a >= b and b >= c):
    (a, b, c) = (c, b, a)
elif (a >= b and b <= c and a >= c):
    (a, b, c) = (b, c, a)
elif (a >= b and b <= c and a <= c):
    (a, b, c) = (b, a, c)
elif (a <= b and b >= c and a <= c):
    (a, b, c) = (a, c, b)
elif (a <= b and b >= c and a >= c):
    (a, b, c) = (c, a, b)
print(a, b, c)
