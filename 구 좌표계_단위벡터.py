from math import *
while True:
    theta=float(input('theta(deg)='))
    #Convert the angle to radian.
    theta=theta*pi/180
    
    phi=float(input('phi(deg)='))
    #Convert the angle to radian.
    phi=phi*pi/180
    #the components of x, y, and z that make up the r-unit vector
    rx,ry,rz=sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta)
    #the components of x, y, and z that make up the theta-unit vector
    tx,ty,tz=cos(theta)*cos(phi),cos(theta)*sin(phi),-sin(theta)
    #the components of x, y, and z that make up the phi-unit vector
    px,py,pz=-sin(phi),cos(phi),0
    
    print('rx(m)={0:11.4f}, ry(m)={1:11.4f}, rz(m)={2:11.4f}'.format(rx,ry,rz))
    print('tx(m)={0:11.4f}, ty(m)={1:11.4f}, tz(m)={2:11.4f}'.format(tx,ty,tz))
    print('px(m)={0:11.4f}, py(m)={1:11.4f}, pz(m)={2:11.4f}'.format(px,py,pz))
