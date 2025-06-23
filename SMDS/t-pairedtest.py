import math
print("Enter The No of Values")
n=int(input()) # 11
print("Enter the L.O.S (Given or Say)")
los=float(input())  # 0.05
print("Enter x values with spaces")
x=list(map(int,input().split())) # 24 17 18 20 19 23 16 18 21 20 19
print("Enter y values with spaces")
y=list(map(int,input().split()))  # 24 20 22 20 17 24 20 20 18 19 22
d=[]   # This is to store the values of the d(i)=x(i)-y(i)
for i in range(n):
    di=x[i]-y[i]
    d.append(di)
print("d values are : ",*d)     # * represents to unpack the elements in the list
print("sigma di value : ",sum(d))
dbar=sum(d)/n  # dbar sumvalue
print("dbar value is :",dbar)
d_dbar_square=[]
d_dsquare=0
for i in range(n):
    d_dbar=d[i]-dbar
    d_dsquare=math.pow(d_dbar,2)
    d_dbar_square.append(d_dsquare)
    d_dsquare=0
print("di-dbar values : ",*d_dbar_square)
d_dsum=sum(d_dbar_square) # di-dbar whole square value
print("sum of di-dbar Value is :",d_dsum)
s_inside=d_dsum/(n-1)
s=math.sqrt(s_inside)  # s value  s=sqrt(sumof di-dbar square/n-1)
print("s value is :",s)
t=dbar/(s/math.sqrt(n))   # t value  t=dbar/s/sqrt(n)
print("calculated t Value is :",abs(t)) # In The t-paired test we take H0 : u=0 and H1 : u>0 => It is Right One Tailed Test
print(f"Now,To Find the tabulated value,from the table check df at t{n-1,los}")
print("Enter the tabulated value ")  # To find whether we should accept H0 or Reject H0
tabt=float(input())
if t<tabt:
    print("Accept H0")
else:
    print("Reject H0") 