from sympy import symbols,Eq,solve
print("Enter the n value")  # No of Values
n=int(input())  # 6
print("Enter the x value") # X value is given in the question
x=int(input()) # 18
print("Enter xi values with spaces")
xi=list(map(int,input().split()))  # 10 12 13 12 16 15
print("Enter yi values with spaces")
yi=list(map(int,input().split()))  # 40 38 43 45 37 43
print("Sum of xi values ",sum(xi))
print("Sum of yi values ",sum(yi))
xiyi=[]
xisqr=[]
yisqr=[]
for i in range(len(xi)):
    rn=xi[i]*yi[i]
    xiyi.append(rn)
    rn=xi[i]*xi[i]
    xisqr.append(rn)
    rn=yi[i]*yi[i]
    yisqr.append(rn)
print("XiYi values ",*xiyi)   # * for unpacking the list
print("XiYi sum ",sum(xiyi))
print("Xi square values ",*xisqr)
print("Xi square sum ",sum(xisqr))
print("Yi square values ",*yisqr)
print("Yi square sum ",sum(yisqr))
a,b=symbols('a b')

#y on x
eq1=Eq( n*a + sum(xi)*b , sum(yi))  # sum(yi)=n*a+sum(xi)*b
eq2=Eq( sum(xi) *a + sum(xisqr) *b ,sum(xiyi))  # sum(xiyi)=sum(xi)*a+sum(xisquare)*b
var=solve((eq1,eq2),(a,b))
print(f"a : {var[a].evalf()},b : {var[b].evalf()}")       # using evalf method to get the values from fraction to decimal......
y=var[a]+var[b]*x
print("y value is (y on x )",y.evalf()) # y=a+bx

# x on y
print("( x on y ) Enter y value given to find x")
y=int(input())
eq1=Eq( n*a + sum(yi)*b , sum(xi))  # sum(xi)=n*a+sum(yi)*b
eq2=Eq( sum(yi) *a + sum(yisqr) *b ,sum(xiyi))  # sum(xiyi)=sum(yi)*a+sum(yisquare)*b
var=solve((eq1,eq2),(a,b))
print(f"a : {var[a].evalf()},b : {var[b].evalf()}")
x=var[a]+var[b]*y
print("x value (x on y)",x.evalf())  # x=a+by