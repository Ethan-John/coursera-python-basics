# Power of 2

N = int(input())
if N < 0 or N > 100:
    print("Степень должна быть > 0 и <= 100! Введите повторно:")
    N = int(input())
    print(2**N)
else:
    print(2**N)
