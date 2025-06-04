print((lambda x,y:(lambda z:[f'{int(x)} * {int(z)} = {int(x)*int(z)}',f'{int(x)} + {int(z)} = {int(x)+int(z)}'][y=='+'])(''.join(reversed(x))))(input(),input()))
