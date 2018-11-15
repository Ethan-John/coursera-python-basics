# Обращение числа

N = int(input())
length = len(str(N))
i = length
k = 0
m = ''
while i > 0:
    k = N % 10
    N = N // 10
    m = m + str(k)
    i -= 1
print(m)
