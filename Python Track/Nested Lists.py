if __name__ == '__main__':
    arr = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    newArr = []
    for i in range(len(arr)):
        newArr.append(arr[i][1])
    arr2 = sorted(newArr)
    arr3 = list(set(arr2))
    number = arr3[1]
    nameList =[]
    for i in range(len(arr)):
        if number == arr[i][1]:
            nameList.append(arr[i][0])
    answer = sorted(nameList)
    for i in answer:
        print(i)
