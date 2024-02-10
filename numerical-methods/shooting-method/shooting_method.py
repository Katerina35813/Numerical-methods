import math as m
a=0
b=1
h0=0.3
gamma0=0
gamma1=m.exp(1)
alpha0=1
betta0=0
alpha1=0
betta1=1
eps=10**(-5)
def f(x:float,u,v:float):
    f=m.exp(x)*(1+x**2)+u-v
    return f
def g(x:float,u,v:float):
    g=x*m.exp(x)+u+v
    return g
def step(x,u,v,h:float):
    f0=h*f(x,u,v)
    F0=h*g(x,u,v)
    f1 = h*f(x + h/2, u + f0/2,v + F0/2)
    F1 = h*g(x + h/2, u + f0/2,v + F0/2)
    f2 = h*f(x + h/2, u+ f1/2,v + F1/2)
    F2 = h*g(x + h/2, u + f1/2,v + F1/2)
    f3 = h*f(x + h, u + f2,v + F2)
    F3 = h*g(x + h, u + f2,v + F2)
    step1 = u + (f0 + 2*f1 + 2*f2 + f3)/6
    step2 = v + (F0 + 2*F1 + 2*F2 + F3)/6
    return [step1,step2]
def jump(x,u,v:float):
    h=h0
    uv1 = step(x,u,v,h) 
    uv2 = step(x,u,v,h/2)
    uv3 = step(x+h/2,u,v,h/2)
    while (abs(uv1[0] -uv3[0]) > eps) and (abs(uv1[1] -uv3[1]) > eps):
        uv1 = uv2
        h = h/2
        uv2 = step(x,u,v,h/2)
        uv3= step(x+h/2,uv2[0],uv2[1],h/2)
    p = uv1 
    return [h,p[0],p[1]]

def F_ksi(ksi:float ):
  x=a
  u=(gamma0-betta0*ksi)/alpha0
  v=ksi
  while x<b :
    list=jump(x,u,v)
    x=x+list[0]
    u=list[1]
    v=list[2]
    print(' h=',list[0],' x=',x,' u=',u,'v= ',v)
    print('err1=',u-x*m.exp(x))
    print('err2=',v-(x**2)*m.exp(x))
    if (b-x)<h0:
        h0=b-x
  Fksi=alpha1*u+betta1*v-gamma1
  return Fksi

def dih(ksi0,ksi1:float):
    c=(ksi0+ksi1)/2
    while abs(ksi0 - ksi1) > eps/10 and F_ksi(c) > eps:
        c = (ksi0 + ksi1) / 2
        if F_ksi(ksi0) * F_ksi(ksi1) < 0:
            ksi1 = c
        else:
            ksi0 = c
    return c         

ksi0 = float(input('Введите ksi0 '))
ksi1 = float(input('Введите ksi1 '))
x=a
while (F_ksi(ksi0)*F_ksi(ksi1)) > 0:
    print("Вилка не образовалась","fksi0",F_ksi(ksi0),"fksi1",F_ksi(ksi1))
    ksi0 = float(input('Введите ksi0 '))
    ksi1 = float(input('Введите ksi1 '))


c=dih(ksi0,ksi1)
print(c)
while (x<b) :
    u=(gamma0-betta0*c)/alpha0
    v=c
    list=jump(x,u,v)
    x=x+list[0]
    u=list[1]
    v=list[2]
    if (b-x)<h0:
        h0=b-x   

print(' h=',list[0],' x=',x,' u=',u,'v= ',v)
print('err1=',u-x*m.exp(x))
print('err2=',v-(x**2)*m.exp(x))