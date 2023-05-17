if __name__ == '__main__':
    N = int(input())
    arr=[]
    for i in range(N):
        inst, *num = input().split()
        arrofInstruction=list(map(int,num))
        if inst=="print":
            print(arr)
        if inst=="insert":
            arr.insert(arrofInstruction[0],arrofInstruction[1])
        elif inst=="remove":
            arr.remove(arrofInstruction[0])
        elif inst=="append":
            arr.append(arrofInstruction[0])
        elif inst=="sort":
            arr.sort()
        elif inst=="pop":
            arr.pop()
        elif inst=="reverse":
            arr.reverse()
