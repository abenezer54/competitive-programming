def swap_case(s):
    arr = []
    for i in s:
        if i.islower():
            i = i.upper()
        elif i.isupper():
            i = i.lower()
        arr.append(i)
    return "".join(arr)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
