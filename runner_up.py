if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    values = [x for x in arr]
    print(sorted(set(values), key=int, reverse=True)[1])
