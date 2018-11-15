# Максимальная длина монотонного фрагмента

N = int(input())
counterUp = 1
counterDown = 1
maxUp = 1
maxDown = 1
while N != 0:
    x = N
    N = int(input())
    if x >= N and N != 0:
        counterUp = 0
    elif x < N:
        counterUp += 1
        if counterUp > maxUp:
            maxUp = counterUp
    if x <= N and N != 0:
        counterDown = 0
    elif x > N:
        counterDown += 1
        if counterDown > maxDown:
            maxDown = counterDown
if maxUp >= maxDown:
    print(maxUp)
else:
    print(maxDown)
