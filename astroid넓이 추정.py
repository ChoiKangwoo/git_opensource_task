def area(x1,y1,x2,y2,x0,y0): # area of a triangle
# x0,y0 = ref. point; x1,y2 = 1st point; x2,y2 = 2nd point
    xx1=x1-x0; yy1=y1-y0; xx2=x2-x0; yy2=y2-y0
    a=(xx1*yy2-xx2*yy1)/2
    return a
from math import *
import math
x=[0]*10000; y=[0]*10000
while True:
    xr,yr=map(float,input('astroid center xr,yr=').split())
    #xr,yr is (0,0) in problem
    a=float(input('astroid radius a='))
    n=int(input('Number of line segments approximating ellipse n(<10000)='))
    for i in range(0,n):
        theta=i*(2*pi/n)
        x[i]=xr+a*math.pow(cos(theta),3); y[i]=yr+a*math.pow(sin(theta),3)
    x[n],y[n]=x[0],y[0]
    s=0
    for i in range(0,n):
        ta=area(x[i],y[i],x[i+1],y[i+1],xr,yr)
        s=s+ta
        print('Triangle no. =',i,'Area of triangle=',ta)
    print('Area of astroid(numerical)=',abs(s))
    print('Area of astroid(theory) =',3*pi*math.pow(a,2)/8)