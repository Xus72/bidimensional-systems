#!/usr/bin/env sage -python

from flask import Flask
from sage.all import *

app = Flask(__name__)

@app.route("/")
def define_system():
    xn,yn = var('xn,yn')
    x = var('x')
    a,b = var('a,b')
    f = b*x+2*(1-b)**(x**2/1+x**2)
    fn = vector([a * yn + f(x=xn), - xn + f(x=xn+1)])
    return xn, yn, fn

@app.route("/")
def fixed_points(fn,a,b,xn,yn):
    sol = solve([fn(a=a,b=b)[0]==xn, fn(a=a,b=b)[1]==yn], xn,yn)
    show(sol)
    return sol

@app.route("/")
def jacobian_matrix(fn,a,b,xn,yn,fix_p):
    fx = fn(a=a,b=b).diff(xn)
    fy = fn(a=a,b=b).diff(yn)
    Df = matrix([fx, fy]).transpose()
    show(Df)
    return Df

@app.route("/")
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

if __name__ == '__main__':
    #app.run(debug=True)

    xn, yn = var('xn,yn')
    x = var('x')
    a, b = var('a,b')
    f = b * x + 2 * (1 - b) ** (x ** 2 / 1 + x ** 2)
    fn = vector([a * yn + f(x=xn), - xn + f(x=xn + 1)])

    sol = fixed_points(fn,0,0,xn,yn)
    df = jacobian_matrix(fn,0,0,xn,yn,sol)
    eigenvalues(sol,df)