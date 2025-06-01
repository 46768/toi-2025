mSize = list(reversed(list(map(int, input().split(' ')))))
b = []
for _ in range(mSize[1]):
    bm = 0
    st = input()
    for s in st.split(' '):
        bm = (bm<<1)+1 if s == '*' else bm<<1
    b.append(bm)
bn = [b[0]]
for i in range(1, mSize[1]):
    bn.append(b[i] | b[i-1])
for i in range(mSize[1]):
    r = []
    rb = bn[i]
    for __ in range(mSize[0]):
        if rb & 1:
            r.append('*')
        else:
            r.append('-')
        rb = rb>>1
    print(' '.join(reversed(r)))
