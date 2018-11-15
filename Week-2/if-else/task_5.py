# Ход короля

c_n1 = int(input())
r_n1 = int(input())
c_n2 = int(input())
r_n2 = int(input())
if (((r_n1 - 1 == r_n2 or r_n1 + 1 == r_n2)) and (((c_n1 - 1 == c_n2) or
                                                   (c_n1 + 1) == c_n2))):
    print('YES')
elif ((r_n1 == r_n2) and ((c_n1 - 1 == c_n2) or (c_n1 + 1) == c_n2)):
    print('YES')
elif ((r_n1 - 1 == r_n2 or r_n1 + 1 == r_n2) and (c_n1 == c_n2)):
    print('YES')
else:
    print('NO')
