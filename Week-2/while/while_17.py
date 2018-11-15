# Номер числа Фибоначчи

A = int(input())
F0 = 0
F1 = 1
i = 0
k = 2
answer = 0
while i < A:
    answer = F0 + F1
    F0 = F1
    F1 = answer
    if A == F1:
        break
    i += F0
    k += 1
if A == answer:
    print(k)
else:
    print(-1)
