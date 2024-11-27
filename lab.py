import math
#Eвтифеева Милана 107б
def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        print("Делить на  0  нельзя")
        return "Делить на  0  нельзя"
    else:
        return a/b

def point_distance(x1,y1,x2,y2):
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    return d

def quad(a,b,c):#ax2+bx+c=0
    if(a!=0):
        D=(b**2)-(4*a*c)
        if (D==0):
            x=(-b)/(2*a)
            return x
        elif(D<0):
            print("Дискриминант меньше нуля. Корней нет")
            return ("Дискриминант меньше нуля. Корней нет")
        else:
            x1=(-b-math.sqrt(D))/(2*a)
            x2=(-b+math.sqrt(D))/(2*a)
            return x1,x2
    else:#xb+c=0
        x=(divide(-c,b))
        return x

def geom_sum(a,q,n):
    return  a*(1-q**n)/(1-q)

