print((lambda x:' '.join([["Red","Green","Blue"][({'R':0,'G':1,'B':2}[x[0]]+i)%3]for i in range(int(x[1]))]))(input().split(' ')))
