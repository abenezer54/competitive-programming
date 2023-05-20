if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArray = sorted(list(set(arr)))
    print(newArray[-2])
