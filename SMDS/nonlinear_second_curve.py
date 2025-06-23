import math
from sympy import symbols,Eq,solve
print("Enter n value")
n=int(input())
print("Enter x value")
x=int(input())
print("Enter xi values with spaces")
xi=list(map(int,input().split()))
print("Enter yi values with spaces")
yi=list(map(int,input().split()))
lnyi=0
xisqr=0
xiyi=0
print(f"{'x=X':<10}{'yi':<10}{'Y=lnyi':<10}{'XiYi':<10}{'Xi^2':<10}")
for i in range(len(xi)):
    print(f"{xi[i]:<10}{yi[i]:<10}{'%.3f'%math.log(yi[i]):<10}{'%.3f'%(xi[i]*math.log(yi[i])):<10}{xi[i]**2:<10}")
    lnyi+=math.log(yi[i])
    xisqr+=xi[i]**2
    xiyi+=xi[i]*math.log(yi[i])
print("Sum of xi ",sum(xi))
print("Sum of Y=lnyi ",lnyi)
print("Sum of XiYi=xilnyi ",xiyi)
print("Sum of XiSquare ",xisqr)
A,B=symbols('A B')
eq1=Eq( n*A + sum(xi)*B,lnyi)
eq2=Eq( sum(xi)*A + xisqr*B,xiyi)
var=solve((eq1,eq2),(A,B)) 
a=math.e ** var[A]
b=math.e ** var[B]  
print(f"a : {a},b : {b}")
y=a*(b ** x )
print("y value is ",y)   # y = a * b power x