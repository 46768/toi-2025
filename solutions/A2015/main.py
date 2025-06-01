print((lambda x,y:(lambda z:z+'\n'+str(int(z)*int(y)))(str(2*int(x[2])*(int(x[0])+int(x[1])))))(input().split(' '),input()))
