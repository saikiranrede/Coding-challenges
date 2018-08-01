N = int(input())
arr = map(int, input().split())
values = [x for x in arr]
values.reverse()
if N > 0 and len(values) > N:
    print(values[N-1])
else:
    print("NIL")
