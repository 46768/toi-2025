n = int(input())
p = []
v = []
for i in range(n):
    s = input().split(' ')
    p.append(int(s[0]))
    v.append(int(s[1]))

p = list(reversed(p))
v = list(reversed(v))

c = 0
u = 0
for i in range(n):
    c = max(c, v[i])
    if c != v[i]:
        u += 1
print(u)
