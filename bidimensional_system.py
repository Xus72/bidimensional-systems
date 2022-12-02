#!/usr/bin/env sage -python
from sage.all import *

'''def define_system():
    xn,yn = var('xn,yn')
    x = var('x')
    a,b = var('a,b')
    f = b*x+2*(1-b)**(x**2/1+x**2)
    fn = vector([a * yn + f(x=xn), - xn + f(x=xn+1)])
    return xn, yn, fn'''

def fixed_points(fn,a,b,xn,yn):
    sol = solve([fn(a=a,b=b)[0]==xn, fn(a=a,b=b)[1]==yn], xn,yn)
    return sol

def jacobian_matrix(fn,a,b,xn,yn,fix_p):
    fx = fn(a=a,b=b).diff(xn)
    fy = fn(a=a,b=b).diff(yn)
    Df = matrix([fx, fy]).transpose()
    show(Df)
    return Df

def eigenvalues(fix_p,df):
    for i in range(len(fix_p)):
        show(df(xn=fix_p[i][0],yn=fix_p[i][1]))
        eigenvalue = [df(xn=fix_p[i][0].right(),yn=fix_p[i][1].right()).eigenvalues()]
        show(eigenvalue)
        for j in range(len(eigenvalue)):
            lambda_1 = eigenvalue[i][0]
            lambda_2 = eigenvalue[i][1]
            show(lambda_1)
            show(lambda_2)
            show(lambda_1.abs().n())
            show(lambda_2.abs().n())
            '''if lambda_1.abs() < 1 & lambda_2.abs() < 1:
                show("The fixed point " + sol[i] + "is a sink point")
            if lambda_1.abs().n() > 1.0 & lambda_2.abs().n > 1.0:
                show("The fixed point " + sol[i] + "is a source point")
            if (lambda_1.abs().n() < 1 & lambda_2.abs().n() > 1) | (lambda_1.abs().n() > 1 & lambda_2.abs().n() < 1):
                show("The fixed point " + sol[i] + "is a saddle point")
            if lambda_1.abs().n() == 1 | lambda_2.abs().n() == 1:
                show("The fixed point " + sol[i] + "is a non-hyperbolic point")'''
    return None

def periodic_points(fn,a,b,xn,yn):
    sol_2_per = solve([fn(xn=fn[0],yn=fn[1],a=a,b=b)[0]==xn, fn(xn=fn[0],yn=fn[1],a=a,b=b)[1]==yn], xn,yn)
    return sol_2_per

def attractors(fn,a,b,xn,yn,x0,n,m):
    points = list()

    for i in range(n-1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1]).n()
    for i in range(n,m+1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1]).n()
        points = [x0]

    return plot(point(points))

def orbits(fn,a,b,xn,yn,x0,n):
    g = Graphics()
    points = [x0]
    g += point(x0,rgcolor='red')

    for i in range(n-1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1])
        points += [x0]
        g += point(x0, rgcolor='red')
    for i in range(n-1):
        g += line([points[i], points[i+1]], rgcolor='blue')

    return g

def final_orbits(fn,a,b,xn,yn,x0,n,m):
    g = Graphics()
    points = list()
    g += point(x0, rgcolor='red')

    for i in range(n-1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1])
    for i in range(n,m+1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1])
        points += [x0]
        g += point(x0, rgcolor='red')
    for i in range(m-n):
        g += line([points[i], points[i+1]], rgcolor='blue')

    return g

if __name__ == '__main__':
    xn, yn = var('xn,yn')
    x = var('x')
    a,b = var('a,b')
    f = b * x + 2 * (1 - b) ** (x ** 2 / 1 + x ** 2)
    fn = vector([a * yn + f(x=xn), - xn + f(x=xn + 1)])
    a = 0
    b = 0
    sol = fixed_points(fn,a,b,xn,yn)
    df = jacobian_matrix(fn,a,b,xn,yn,sol)
    eigenvalues(sol,df)
    sol_f2 = periodic_points(fn,a,b,xn,yn)
    show(sol_f2)
    df2 = jacobian_matrix(fn,a,b,xn,yn,sol_f2)
    show(df2)
    eigenvalues(sol_f2,df2)

