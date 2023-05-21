# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = set()
for i in range(n-1):
    arr.add(input())
arr2 = list(arr)
print(len(arr2))
