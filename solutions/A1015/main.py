print((lambda x,y,z:[x[0]+z+y[-1],x[:2]+y[-1]+z][(len(x)>5)and(len(y)>5)])(input(),input(),input()))
