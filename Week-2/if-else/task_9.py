# Коровы

n = int(input())
if n == 1:
    print(n, 'korova')
elif n >= 2 and n < 5:
    print(n, 'korovy')
elif n > 11 and str(n).endswith('1'):
    print(n, "korova")
elif (n > 14 and (str(n).endswith('2') or
                  str(n).endswith('3') or str(n).endswith('4'))):
    print(n, 'korovy')
elif n >= 5:
    print(n, "korov")
