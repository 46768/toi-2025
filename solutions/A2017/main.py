print((lambda x,y:{'R':{'S':60,'M':80,'L':100},'T':{'S':80,'M':100,'L':120}}[x[1].upper()][x[0].upper()]+{'N':0,'P':15,'E':10}[y[0].upper()]*int(y[1]))(input().split(' '),(input()+' 0').split(' ')))
