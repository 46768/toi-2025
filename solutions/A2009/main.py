s = input().split(' ')
n = int(s[0])
p = int(s[1])-1
wt = []
for i in range(n):
    ww = list(map(lambda x: int(x)-1, input().split(' ')))
    wt.append(ww)

c = list(range(n))
w = []

while len(c) != 1:
    for i in range(0, len(c), 2):
        t1 = c[i]
        t2 = c[i+1]
        wl = wt[t1][t2]
        w.append(wl if (t1 if wl == t2 else t2) != p else p)
        if (t1 if wl == t2 else t2) == p:
            p = -1
    c = w
    w = []

print(c[0]+1)
