from sympy import symbols,Eq,solve
print("Enter the n value")  # No of Values
n=int(input())  # 7
print("Enter the x value") # X value is given in the question
x=int(input()) # 13
print("Enter xi values with spaces")
xi=list(map(int,input().split()))  # 2 4 6 8 10 12 14
print("Enter yi values with spaces")
yi=list(map(int,input().split()))  # 4 2 5 10 4 11 12
xisqr=0
xiyi=0
xicub=0        # :<10 for the coloum alignment
xisqryi=0      # f means format
xiquad=0
print(f"{'xi':<10}{'yi':<10}{'xi^2':<10}{'xi*yi':<10}{'xi^3':<10}{'xi^2*yi':<10}{'xi^4':<10}")
for i in range(len(xi)):
    print(f"{xi[i]:<10}{yi[i]:<10}{xi[i]**2:<10}{xi[i]*yi[i]:<10}{xi[i]**3:<10}{xi[i]**2*yi[i]:<10}{xi[i]**4:<10}")
    xisqr+=xi[i]*xi[i]
    xiyi+=xi[i]*yi[i]
    xicub+=xi[i]*xi[i]*xi[i]
    xisqryi+=xi[i]*xi[i]*yi[i]
    xiquad+=xi[i]**4
print("Sum of xi values ",sum(xi))
print("Sum of yi values ",sum(yi))
print("Sum of XiSquare ",xisqr)
print("Sum of XiYi",xiyi)
print("Sum of XiCube ",xicub)
print("Sum of XiSquare*Yi ",xisqryi)
print("Sum of XiQuad ",xiquad)

a,b,c=symbols('a b c')

# y on x
eq1=Eq( n*a + sum(xi)*b + xisqr*c , sum(yi))    # sum(yi)=n*a+sum(xi)*b+sum(xisquare)*c
eq2=Eq( sum(xi) *a + xisqr *b + xicub*c ,xiyi)     # sum(xiyi)=sum(xi)*a+sum(xisquare)*b+sum(xicube)*c
eq3=Eq( xisqr*a + xicub*b + xiquad*c ,xisqryi) 
var=solve((eq1,eq2,eq3),(a,b,c))       # using evalf method to get the values from fraction to decimal
print(f"a : {var[a].evalf()},b : {var[b].evalf()},c : {var[c].evalf()}")
y=var[a]+var[b]*x+var[c]*x**2  # y = a + bx + cxsquare
print("y value is (y on x )",y.evalf())