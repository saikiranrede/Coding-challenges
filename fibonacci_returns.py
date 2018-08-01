def fib(value):
    a,b= 0,1
    while value!=0:
        a,b = b,a+b
        value-=1
    return a

arr = []
i= 0
while i != '':
    i = input()
    if i =='':
        break
    else:
        i =int(i)
        arr.append(i)

for i in arr:
    print(fib(i))


"""
def fib(value):
    a,b= 0,1
    while value!=0:
        a,b = b,a+b
        value-=1
    return a
i= 0
arr = []
while i != '':
    try:
        i = input()
        i =int(i)
        arr.append(i)
    except (EOFError):
        break

for i in arr:
    print(fib(i))

"""
