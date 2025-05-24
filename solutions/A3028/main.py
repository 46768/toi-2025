bSize = list(map(int, input().split(" ")))
mc = int(input())
mines = {}
for _ in range(mc):
    mine = input().split(" ")
    if int(mine[0]) not in mines:
        mines[int(mine[0])] = set()
    mines[int(mine[0])].add(int(mine[1]))

for y in range(bSize[0]):
    row = []
    for x in range(bSize[1]):
        if y in mines:
            if x in mines[y]:
                row.append('x')
                continue
        cnt = 0
        for it in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
            if it[1] in mines:
                if it[0] in mines[it[1]]:
                    cnt += 1
        row.append(str(cnt))
    print(' '.join(row))
