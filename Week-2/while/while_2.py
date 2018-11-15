# Минимальный делитель

N = int(input())
minDiv = N
i = N
while i > 1:
    if N % i == 0:
        if i < minDiv:
            minDiv = i
    i -= 1
print(minDiv)
