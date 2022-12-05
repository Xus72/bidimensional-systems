#!/usr/bin/env sage -python

from flask import Flask, render_template, request, flash, redirect
from bidimensional_system import fixed_points, define_system, jacobian_matrix, eigenvalues, periodic_points, attractors
from sage.all import *
from bokeh.io import show
from bokeh.models.text import MathText
from bokeh.embed import components
from bokeh.plotting import figure, output_file, show
from bokeh.resources import INLINE

app = Flask(__name__)

xn, yn, fn, a, b = define_system()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def set_params():
    global a,b
    if request.method == "POST":
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
    return render_template("index.html")

@app.route("/fixed_point")
def fixed_point():
    sol = fixed_points(fn,a,b,xn,yn)
    print(sol)
    df = jacobian_matrix(fn,a,b,xn,yn)
    print(df)
    eigenval = eigenvalues(sol,df)
    return render_template("fixed_point.html", sol=sol,df=df, eigenval=eigenval)

@app.route("/periodic_point")
def periodic_point():
    sol2 = periodic_points(fn,a,b,xn,yn)
    df2 = jacobian_matrix(fn,a,b,xn,yn)
    eigenval2 = eigenvalues(sol2,df2)
    return render_template("periodic_point.html", sol=sol2, df=df2, eigenval=eigenval2)

@app.route("/orbits")
def draw_orbits():
    x0 = [3,1]
    n = 5000
    p = figure(width=400, height=400)
    x = list()
    y= list()
    x.append(x0[0])
    y.append(x0[1])

    for i in range(n-1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1])
        x.append(float(x0[0]))
        y.append(float(x0[1]))
    p.circle(x=x,y=y,color='red',size=8)
    p.line(x=x,y=y,color='blue', line_width=2)

    script, div = components(p)

    return render_template("orbits.html", plot_script=script, plot_div = div, js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),).encode('UTF-8')

@app.route("/final_orbits")
def draw_final_orbits():
    x0 = [3,1]
    n = 2000
    m = 3000
    p = figure(width=400, height=400)
    x = list()
    y= list()
    l_x = list()
    l_y = list()

    for i in range(n-1):
        x0 = fn(a=a,b=b,xn=x0[0],yn=x0[1])
    for i in range(n,m+1):
        x0 = fn(a=a, b=b, xn=x0[0], yn=x0[1])
        x.append(float(x0[0]))
        y.append(float(x0[1]))
    p.circle(x=x,y=y,color='red',size=6)
    for i in range(m-n):
        l_x.append(x[i+1])
        l_y.append(y[i+1])
    p.line(x=l_x,y=l_y,color='blue', line_width=2)

    script, div = components(p)

    return render_template("final_orbits.html", plot_script=script, plot_div = div, js_resources=INLINE.render_js(),
        css_resources=INLINE.render_css(),).encode('UTF-8')

@app.route("/attractor")
def attractor():
    x0 = [3, 5]
    n = 2000
    m = 3000
    p = figure(width=400, height=400)
    x = list()
    y = list()
    x.append(x0[0])
    y.append(x0[1])

    for i in range(n - 1):
        x0 = fn(a=a, b=b, xn=x0[0], yn=x0[1])
    for i in range(n, m + 1):
        x0 = fn(a=a, b=b, xn=x0[0], yn=x0[1])
        x.append(float(x0[0]))
        y.append(float(x0[1]))
    p.circle(x=x, y=y, color='red', size=6)

    script, div = components(p)
    return render_template("final_orbits.html", plot_script=script, plot_div=div, js_resources=INLINE.render_js(),
                           css_resources=INLINE.render_css(), ).encode('UTF-8')

if __name__ == '__main__':
    app.run(debug=True)
