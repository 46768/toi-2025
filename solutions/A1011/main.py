print((lambda z:''.join([str(i)+c for c,i in z.items()]))((lambda x,y:([(y.update({c:y.get(c,0)+1}))for c in x],y)[1])(input(),{})))
