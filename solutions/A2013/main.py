print(sum([(lambda x: {'H':5,'O':3,'J':2}[x[0]]*int(x[1]))(input().split(' ')), (lambda x: {'R':[12,18,25],'T':[15,20,30],'M':[10,15,20]}[x[0]][int(x[1])-1]*int(x[2]))(input().split(' '))]))
