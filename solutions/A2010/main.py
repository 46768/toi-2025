s = input().split(' ')
n = int(s[0])
q = int(s[1])
w = {0: 99999999}
d = 0
dm = 0
for i in range(n):
    s = input().split(' ')
    dd = int(s[0])
    ll = int(s[1])
    d += dd
    dm = max(dm, d)
    if d not in w:
        w[d] = 0
    w[d] += ll

print(w)
for i in range(q):
    dd = dm
    ws = w[dd]
    ww = int(input())
    while ww > ws:
        dd -= 1
        ws += w[dd]
    print(dd)
