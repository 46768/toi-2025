from random import randint

bx = 100#randint(3, 100)
by = 30#randint(3, 100)
mines = []
for _ in range(bx):
    mines.append(randint(0, (2**by)-1))
print(str(bx)+' '+str(by))
for i in range(bx):
    r = []
    rb = mines[i]
    for __ in range(by):
        if rb & 1:
            r.append('*')
        else:
            r.append('-')
        rb = rb>>1
    print(' '.join(reversed(r)))
