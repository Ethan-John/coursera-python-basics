# Четные индексы

checkList = list(map(int, input().split()))
for i in range(len(checkList)):
    if i % 2 == 0:
        print(checkList[i])
