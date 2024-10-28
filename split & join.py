def split_and_join(line):
    k = line.split()
    s = "-".join(k)
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
