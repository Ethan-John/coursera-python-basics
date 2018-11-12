# Symmetric

N = int(input())
n1 = N // 1000
n2 = N // 100 % 10
n3 = N // 10 % 10
n4 = N % 10
if (n1 == n4 and n2 == n3):
    print(1)
else:
    print(11)
