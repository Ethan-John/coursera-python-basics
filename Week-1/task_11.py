# Clocks

N = int(input())
if N >= 1440:
    N = N % 1440
print(N // 60, N % 60)
