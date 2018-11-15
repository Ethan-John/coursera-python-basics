# Координатные четверти


def part(x, y):
    if x > 0:
        if y > 0:
            s = 1
        elif y < 0:
            s = 4
    if x < 0:
        if y > 0:
            s = 2
        elif y < 0:
            s = 3
    else:
        s = 0
    return s

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (part(x1, y1) == part(x2, y2)):
    print('YES')
else:
    print('NO')
