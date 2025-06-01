t = input()
a = input()

if t[0] == a[0]:
    if t[2:] == a[2:]:
        print(1000000)
    elif t[4:] == a[4:]:
        print(2000)
    elif t[5:] == a[5:]:
        print(1000)
    else:
        print(20)
else:
    if t[2:] == a[2:]:
        print(100000)
    elif t[4:] == a[4:]:
        print(200)
    elif t[5:] == a[5:]:
        print(100)
    else:
        print(0)
