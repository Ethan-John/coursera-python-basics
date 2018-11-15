# Количество палиндромов

N = int(input())
i = 1
counter = 0
while i <= N:
    length = len(str(i))
    j = length
    m = ''
    number = i
    while j > 0:
        k = number % 10
        number = number // 10
        m = m + str(k)
        j -= 1
    if int(m) == i:
        counter += 1
    i += 1
print(counter)
