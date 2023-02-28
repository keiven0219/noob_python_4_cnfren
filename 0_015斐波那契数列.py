#斐波那契数列
a,b = 0,1
while a+b <= 100:
    print(b,end=',')
    a, b = b, a + b