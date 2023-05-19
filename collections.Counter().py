# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
numofShoes = int(input())
listofShoes = Counter(list(map(int,input().split())))
numofCustomers = int(input())
money = 0
for i in range(numofCustomers):
    a, b = list(map(int, input().split()))
    for j in listofShoes.keys():
        if a == j and listofShoes[j] > 0:
            money += b
            listofShoes[j] -= 1
print(money)
