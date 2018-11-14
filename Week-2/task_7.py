# Цвет клеток шахматной доски


def black_or_white(raw, column):
    is_black = False
    if raw == column:
        is_black = True
    elif (((raw % 2 == 1) and (column % 2 == 1)) or
          ((raw % 2 == 0) and (column % 2 == 0))):
        is_black = True
    return is_black

raw1 = int(input())
column1 = int(input())
raw2 = int(input())
column2 = int(input())
if ((black_or_white(raw1, column1) == black_or_white(raw2, column2))):
    print('YES')
else:
    print('NO')
