#!/usr/bin/env sage -python

from flask import Flask, render_template, request, flash, redirect
from bidimensional_system import fixed_points, define_system, jacobian_matrix, eigenvalues
from sage.all import *
from bokeh.io import show
from bokeh.models.text import MathText
from bokeh.embed import components
from bokeh.plotting import figure

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
    df = jacobian_matrix(fn,a,b,xn,yn,sol)
    eigenval = eigenvalues(sol,df)
    return render_template("fixed_point.html", sol=sol,df=df, eigenval=eigenval)


if __name__ == '__main__':
    app.run(debug=True)
