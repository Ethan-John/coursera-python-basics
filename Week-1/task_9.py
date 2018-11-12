# Three-digit number

N = int(input())

n1 = N % 10
n2 = N // 10 % 10
n3 = N // 10 // 10
print(n1+n2+n3)
