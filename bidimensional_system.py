#!/usr/bin/env sage -python
from sage.all import *

def define_system():
    x, y = var('x,y')
    a, b = var('a,b')
    f = b * x + 2 * (1 - b) ** (x ** 2 / 1 + x ** 2)
    fn = vector([a * y + f(x=x), - x + f(x=x)])
    return x, y, fn, a, b

def fixed_points(fn,x,y):
    sol = solve([fn[0]==x, fn[1]==y], x,y)
    return sol

def jacobian_matrix(f,x,y,fix_p):
    fx = f.diff(x)
    fy = f.diff(y)
    Df = matrix([fx, fy]).transpose()
    Df = Df(x=fix_p[0],y=fix_p[1])
    return Df

def eigenvalues(fix_p,df):
    eigenval_abs = list()
    for i in range(len(fix_p)):
        d = df(x=fix_p[i][0],y=fix_p[i][1])
        eigenvalue = [d.eigenvalues()]
        for j in range(len(eigenvalue)):
            lambda_1 = eigenvalue[i][0].abs().n()
            lambda_2 = eigenvalue[i][1].abs().n()
            eigenval_abs.append([lambda_1,lambda_2])
    return eigenval_abs

def periodic_points(fn,x,y):
    sol_2_per = solve([fn(x=fn[0],y=fn[1])[0]==x, fn(x=fn[0],y=fn[1])[1]==y], x,y)
    return sol_2_per

def jacobian_matrix_2(f,x,y,fix_p):
    Df = jacobian_matrix(f,x,y,fix_p)
    Df2 = Df(x=fix_p[0], y=fix_p[1])*Df(x=fix_p[1],y=fix_p[0])
    return Df2
def eigenvectors(df,fix_p):
    eigenvector = list()
    for i in range(len(fix_p)):
        eigenvector_left = df(x=fix_p[i][0],y=fix_p[i][1]).eigenvectors_left()
        eigenvector_right = df(x=fix_p[i][0],y=fix_p[i][1]).eigenvectors_left()
        eigenvector.append(eigenvector_left,eigenvector_right)
    return eigenvector

'''def varieties(fn,a,b,xn,yn,fix_p,df):
    if (eigenvalues(fix_p,df)[0] < 1 & eigenvalues(fix_p,df)[1]) > 1 | (eigenvalues(fix_p,df)[0] > 1 & (eigenvalues(fix_p,df))[1]):
        eigenvector = eigenvectors(df,fix_p)'''
