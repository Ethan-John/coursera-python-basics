# Total cost

A = int(input())
B = int(input())
N = int(input())
cost = A * 100 + B
total_cost = cost * N
print(total_cost // 100, total_cost % 100)
