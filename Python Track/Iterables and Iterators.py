# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
num = int(input())
letters = list(input().split())
indices = int(input())
arr =list(combinations(letters, indices))
counter=0

for i in range(len(arr)):
    if "a" in list(arr[i]):
        counter+=1
        
        
print(round(counter/len(arr), 12))
