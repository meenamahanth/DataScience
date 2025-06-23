import math
from sympy import symbols,Eq,solve
print("Enter n value")
n=int(input())
print("Enter x value")
x=int(input())
print("Enter xi values with spaces")
xi=list(map(int,input().split()))
print("Enter yi values with spaces")
yi=list(map(float,input().split()))
lnxi=0
lnyi=0
xisqr=0
xiyi=0
print(f"{'x=X':<10}{'yi':<10}{'Xi=lnxi':<10}{'Y=lnyi':<10}{'XiYi':<10}{'Xi^2':<10}")
for i in range(len(xi)):
    print(f"{xi[i]:<10}{yi[i]:<10}{'%.3f'%math.log(xi[i]):<10}{'%.3f'%math.log(yi[i]):<10}{'%.3f'%(math.log(xi[i])*math.log(yi[i])):<10}{'%.3f'%math.log(xi[i])**2:<10}")
    lnxi+=math.log(xi[i])
    lnyi+=math.log(yi[i])
    xisqr+=math.log(xi[i])**2
    xiyi+=math.log(xi[i])*math.log(yi[i])
print("Sum of Xi=lnxi ",lnxi)
print("Sum of Y=lnyi ",lnyi)
print("Sum of XiYi=lnxilnyi ",xiyi)
print("Sum of XiSquare ",xisqr)
A,B=symbols('A B')
eq1=Eq( n*A + lnxi*B,lnyi)
eq2=Eq( lnxi*A + xisqr*B,xiyi)
var=solve((eq1,eq2),(A,B)) 
a=math.e ** var[A]
b=var[B]   # loge with base 10 value is 0.4343 
print(f"a : {a},b : {b}")
y=a * ( x ** b ) 
print("y value is ",y) # y = a * x power b