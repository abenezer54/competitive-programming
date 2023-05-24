#Using Ceil() function
from math import ceil
m, n, a = list(map(int, input().split()))
print(ceil(m/a)*ceil(n/a))
#Using Loop
# row = 0
# column = 0
# for i in range(1, m):
#     if i * a >= m:
#         row = i
#         break
# for i in range(1, n):
#     if i * a >= n:
#         column = i
#         break
# print(column * row)
