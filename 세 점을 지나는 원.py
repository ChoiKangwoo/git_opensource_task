# Find the center and the radius of a circle defined by 3 points
def unit(x,y,z):
    r=sqrt(x**2+y**2+z**2);return x/r,y/r,z/r
def mag(x,y,z):
    return sqrt(x**2+y**2+z**2)
def dot(ax,ay,az,bx,by,bz):
    return ax*bx+ay*by+az*bz
def cross(ax,ay,az,bx,by,bz):
    return ay*bz-az*by,az*bx-ax*bz,ax*by-ay*bx

from math import *
while True:
    x1,y1=map(float,input('x1,y1=').split())
    x2,y2=map(float,input('x2,y2=').split())
    x3,y3=map(float,input('x3,y3=').split())
 
    #u is unit vector r2->r1
    ux,uy,uz=unit(x1-x2,y1-y2,0)
    #w is unit vector r2->r3
    wx,wy,wz=unit(x3-x2,y3-y2,0)
    #w1 is result of cross product : wXu
    wx1,wy1,wz1=cross(wx,wy,wz,ux,uy,uz)
    # redefine w vector w1's unit vector
    wx,wy,wz=unit(wx1,wy1,wz1)
    #u and v are at right angles.==>othogonal vector
    vx,vy,vz=cross(wx,wy,wz,ux,uy,uz)
    #u1 is the component of the u vector of the r2->r1 vector.
    u1=dot(x1-x2,y1-y2,0,ux,uy,uz)
    #u3 is the component of the u vector of the r2->r3 vector.
    u3=dot(x3-x2,y3-y2,0,ux,uy,uz)
    #v3 is the component of the v vector of the r2->r3 vector.
    v3=dot(x3-x2,y3-y2,0,vx,vy,vz)
    #Using Radius and Diameter Ratio (2:1)
    u0=u1/2
    v0=((u3-u0)**2+v3**2-u0**2)/(2*v3)
    r=sqrt(u0**2+v0**2)
    print('Method-1: r=',r)
    r=mag(x1-x2,y1-y2,0)*mag(x3-x2,y3-y2,0)*mag(x3-x1,y3-y1,0)

    cx,cy,cz=cross(x1-x2,y1-y2,0,x3-x2,y3-y2,0)
    r=r/(2*mag(cx,cy,cz))
    print('Method-2: r=',r)
    cx=x2+u0*ux+v0*vx;cy=y2+u0*uy+v0*vy;cz=0+u0*uz+v0*vz
    print('Center: cx,cy,cz={0:11.4f}{1:11.4f}{2:11.4f}'.format(cx,cy,cz))
    r1=mag(x1-cx,y1-cy,0-cz);r2=mag(x2-cx,y2-cy,0-cz);r3=mag(x3-cx,y3-cy,0-cz)
    print('Check: r1,r2,r3={0:11.4f}{1:11.4f}{2:11.4f}'.format(r1,r2,r2))
 
    ur1,ur2=map(float,input('ur1,ur2=').split())
    if abs(mag(ur1-cx,ur2-cy,0-cz)) >r:
        print("r is outside of circle")
    elif abs(mag(ur1-cx,ur2-cy,0-cz)) < r:
        print("r is inside of cicrcle")
    else:
        print("r is on circle")
