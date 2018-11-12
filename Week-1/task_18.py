# Clocks-2

N = int(input())
if N >= 86400:
    N = N % 86400
hour = N // 3600
minute1 = N // 60 % 60 % 10
minute2 = N // 60 % 60 // 10 % 10
second1 = N % 60 % 10
second2 = N % 60 // 10 % 10
print(hour, str(minute2)+str(minute1), str(second2)+str(second1), sep=':')
