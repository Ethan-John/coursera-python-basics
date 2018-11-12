# Snail

H = int(input())
A = int(input())
B = int(input())
days = (H // (A - B) - (A - (H % (A - B))) // (A - B)) + 1
print(days)
