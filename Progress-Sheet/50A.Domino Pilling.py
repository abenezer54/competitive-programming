n, m = list(map(int,input().split()))
if n*m %2 == 0:
    print(int(n*m/2))
else:
    print(n*m//2)
