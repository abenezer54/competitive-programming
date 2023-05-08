def split_and_join(line):
    # write your code here
    y = line.split(" ")
    z = "-".join(y)
    return z
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
