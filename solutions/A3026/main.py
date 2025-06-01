mSize = list(list(map(int, input().split(' '))))
b1 = []
b2 = []
b3 = []
for _ in range(mSize[0]):
    b1.append(input())
for _ in range(mSize[0]):
    b2.append(input())
for i in range(mSize[0]):
    r = ''
    for j in range(mSize[1]):
        if b1[i][j] == '-':
            r += b2[i][j]
            continue
        if b2[i][j] == '-':
            r += b1[i][j]
            continue
        r += '*'
    b3.append(r)
print('\n'.join(b3))
