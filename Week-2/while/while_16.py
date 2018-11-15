# Числа Фибоначчи

N = int(input())
F0 = 0
F1 = 1
i = 2
answer = 0
while i <= N:
    answer = F0 + F1
    F0 = F1
    F1 = answer
    i += 1
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    print(answer)
