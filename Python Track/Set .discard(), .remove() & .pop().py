n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    cmd, *num = input().split()
    num2 = list(map(int, num))
    if cmd == "pop":
        s.pop()
    elif cmd == "discard":
        s.discard(num2[0])
    elif cmd == "remove":
        s.remove(num2[0])
      
summ = sum(list(s))
print(summ)
