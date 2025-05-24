from random import randint

bx = 100#randint(3, 100)
by = 1000#randint(3, 100)
mc = randint(1, (bx*by)//2)
mines = []
for _ in range(mc):
    mine = str(randint(0, bx-1))+' '+str(randint(0, by-1))
    if mine not in mines:
        mines.append(mine)
    else:
        mc -= 1
print(str(bx)+' '+str(by))
print(mc)
print('\n'.join(mines))
