a=float(input())
b=float(input())
c=float(input())
d=b**2-4*a*c
if d>0:
    x1=(-b+math.sqrt(discr)) / (2*a)
    x2=(-b - math(discr)) / (2*a)
    print(x1,x2)
elif d == 0:
    x=-b/(2*a)
    print(x)