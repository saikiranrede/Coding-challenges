if __name__ == '__main__':
    val = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        val.append([name, score])
    second_highest = sorted(list(set([x for y, x in val])))[1]
    print('\n'.join([a for a,b in sorted(val) if b == second_highest]))
